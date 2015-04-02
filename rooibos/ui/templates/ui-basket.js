{% load staticfiles %}

function basket_imgs_first_row_top() {
    return ($("#basket-thumbs").find("img:visible:first").position() || Object({top: 0})).top;
}

function basket_scroll_arrows() {

    $("#basket-scroll-left").css("visibility", ($("#basket-thumbs").find("img:hidden:first").length > 0) ? "visible" : "hidden");
    var first_row_top = basket_imgs_first_row_top();
    $("#basket-scroll-right").css("visibility", ($("#basket-thumbs")
        .find("img")
        .filter(function () {
            return ($(this).position().top > first_row_top);
        }).length > 0) ? "visible" : "hidden");
}

function recordSelection(ids, checked) {
    var method = ids == 0 ? 'GET' : 'POST';
    if (ids.constructor != Array) ids = [ids];
    ids = $.map(ids, function (e) {
        return parseInt(e);
    });
    ajaxInteractionManager.add({
        type: method,
        url: '{% url 'ui-api-select-record' %}',
        data: {'id': JSON.stringify(ids), 'checked': checked},
        dataType: 'json',
        success: function (r) {
            var basket_thumbs = $("#basket-thumbs");
            basket_thumbs.html(r.basket);
            add_metadata_popup(basket_thumbs);
            $("#basket-header").html(r.header);
            // set up scroll arrows after a delay to give Safari time to load thumbnails first
            setTimeout(basket_scroll_arrows, 1000);
            $("#basket-thumbs").trigger('update');
        }
    });
}

function bindSelectRecordCheckboxes() {
    $(".record-select").click(function () {
        recordSelection($(this).attr('value'), $(this).attr('checked'));
    });
}


function add_metadata_popup(context) {
    $(".metadata-anchor[id*=record-id-]", context).not(".no-metadata-popup").each(function () {
        var anchor = $(this);
        var id = anchor.attr("id");
        id = id.substring(id.lastIndexOf('-') + 1);
        anchor.qtip({
            content: {
                url: '{% url 'data-record-preview' 0 %}'.replace('/0/', '/' + id + '/')
            },
            show: {
                delay: 1000,
                solo: true
            },
            hide: {
                delay: 250,
                fixed: true
            },
            position: {
                corner: {
                    tooltip: 'bottomLeft',
                    target: 'topRight'
                },
                adjust: {
                    screen: true
                }
            },
            style: {
                border: {
                    radius: 4
                },
                fontSize: 'smaller',
                tip: true,
                name: 'cream',
                width: 380
            }
        });
    });
}

add_metadata_popup();


function store_profile_setting(key, value) {
    ajaxInteractionManager.add({
        type: 'POST',
        url: '{% url 'userprofile-store' %}',
        data: {'key': key, 'value': value},
        dataType: 'json'
    });
}

function process_facets() {
    var freqs = Object();

    function sortByFreq(a, b) {
        var fa = freqs[a.id];
        var fb = freqs[b.id];
        return ((fa > fb) ? -1 : ((fa < fb) ? 1 : 0));
    }

    $(".facet .facet-body .facet-line")
        .each(function (i, facetline) {
            var f = $(facetline).contents().eq(2).text().replace(/,/, "");
            freqs[facetline.id] = f ? parseInt(f) : 0;
        }).hover(
        function () {
            $(this).find(".facet-exclude").css('visibility', 'visible');
        },
        function () {
            $(this).find(".facet-exclude").css('visibility', 'hidden');
        }
    );

    $(".facet .facet-body").each(function (i, facet) {
        var terms = $.makeArray($(".facet-line", facet)).sort(sortByFreq).slice(10);
        if (terms.length) {
            $(terms).hide();
            $(".facet-more", facet).click(function () {
                $(this).hide();
                $(terms).show();
                return false;
            }).show();
        }
    });

    $(".facet-header.collapsed").next().hide();

    $(".facet-header").each(function () {
        var id = $(this).parent().attr('id');
        if (id) {
            var s = profile_settings['ui_' + id];
            if (s == "true")
                $(this).next().show();
            else if (s == "false")
                $(this).next().hide();
        }
    }).click(function () {
        var id = $(this).parent().attr('id');
        if (id) store_profile_setting('ui_' + id, $(this).next().is(':hidden'));
        $(this).next().toggle('fast');
        return false;
    }).css('cursor', 'pointer').children().click(function (event) {
        event.stopPropagation();
        /* to keep links in facet header working */
    });

    $(".facet .facet-body .facet-line .facet-exclude").css('visibility', 'hidden');
};

function addCopyLinkIcon(item) {
    if (!item.attr('href') || item.hasClass('nocopylink')) return;
    var host = window.location.href.substring(0, window.location.href.length - window.location.pathname.length - window.location.search.length);
    var url = host + item.attr('href').replace(/\?.+/, '');
    var link = $("<img class='item-action-link' src='{% static 'images/link.png' %}' />");
    link.qtip({
        content: "Copy and paste this URL to link to this item:<br /><input type='text' style='width: 285px;' readonly='readonly' value='" + url + "' />",
        show: {
            delay: 0,
            solo: true,
            when: {
                event: 'click'
            }
        },
        hide: {
            delay: 250,
            fixed: true,
            when: {
                event: 'unfocus'
            }
        },
        position: {
            corner: {
                tooltip: 'bottomLeft',
                target: 'topRight'
            },
            adjust: {
                screen: true
            }
        },
        style: {
            border: {
                radius: 4
            },
            fontSize: 'smaller',
            tip: false,
            name: 'cream',
            width: 320
        }
    });
    link.insertAfter(item);
}

function keepAtTop(element, not_past) {
    if (!keepAtTop.elements) keepAtTop.elements = Array();
    keepAtTop.elements.push(
        element.css("position", "relative").css("top", "0").css('z-index',
                100 - keepAtTop.elements.length).css("left", "0"));
    var placeholder = $("<div>").css("height", element.outerHeight(true)).insertBefore(element).hide();
    keepAtTop.$window = $(window).scroll(function () {
        if (element.is(":hidden")) return;
        var not_past_bottom = not_past ? not_past.offset().top + not_past.height() : Number.MAX_VALUE;
        var offset = 0;
        $.each(keepAtTop.elements, function (i, e) {
            if (e != element) offset += e.is(":visible") ? e.height() : 0;
            else return false;
        });
        var top;
        if (element.css("position") != "fixed") {
            top = element.offset().top;
            // check to see if element is now too far up
            if (top < keepAtTop.$window.scrollTop() + offset &&
                keepAtTop.$window.scrollTop() + offset + element.height() < not_past_bottom) {
                element.css("position", "fixed").css("top", offset + "px").css("width", "100%");
                placeholder.show();
            }
        } else {
            top = placeholder.offset().top;
            // check if element can go back into its normal position
            if (top >= keepAtTop.$window.scrollTop() + offset ||
                element.offset().top + element.height() >= not_past_bottom) {
                element.css("position", "relative").css("top", "0").css("width", "auto");
                placeholder.hide();
            }
        }
    });
}

$(document).ready(function () {
    var timeouts = Object();
    var in_header = $("#header");
    var resetwidth = function () {
        $(this).width($(this).parent().width() + 50);
    };
    in_header.find("ul.menu").each(resetwidth).hide();
    in_header.find(">ul>li:has(ul)").mouseenter(function () {
        clearTimeout(timeouts[$(this)]);
        in_header.find(">ul>li").not($(this))
            .removeClass("selected")
            .children("ul")
            .stop()
            .attr("style", "")
            .hide().each(resetwidth);
        if (!($(this).hasClass("selected"))) $(this).addClass("selected").children("ul").slideDown(200);
    }).mouseleave(function () {
        var lthis = $(this);
        timeouts[lthis] = setTimeout(function () {
            lthis.removeClass("selected").children("ul").hide();
        }, 1000);
    });
    $("#header .search span").mouseenter(function () {
        $("#header .search span,#header .search form").toggle();
    });

    $("#quicksearch").hint();

    function hideBasket(immediate) {
        if (basket_open) return;
        $("#basket-toggle").text("Show");
        if (immediate)
            $("#basket-content").hide();
        else
            $("#basket-content").slideUp();
    }

    function showBasket() {
        $("#basket-toggle").text("Hide");
        $("#basket-content").slideDown();
        basket_scroll_arrows();
    }

    $("#basket-toggle").click(function (e) {
        e.preventDefault();
        basket_open = !basket_open;
        store_profile_setting('ui_basket_open', basket_open);
        if (basket_open) showBasket(); else hideBasket();
    });

    if (!basket_open) {
        hideBasket(true);
    }
    $("#basket-scroll-right").click(function () {
        var first_row_top = basket_imgs_first_row_top();
        if ($("#basket-thumbs img:visible").filter(function () {
            return ($(this).position().top > first_row_top);
        }).length > 0) {
            var last = 0;
            $("#basket-thumbs img:visible").filter(function () {
                return ($(this).position().top <= first_row_top);
            }).each(
                function (i) {
                    $(this).delay(20 * i).hide(0);
                    last = i;
                });
            setTimeout(basket_scroll_arrows, (last + 1) * 20);
        }
    });
    $("#basket-scroll-left").click(function () {
        var first_row_top = basket_imgs_first_row_top();
        if ($("#basket-thumbs img:hidden").length > 0) {
            var first = $("#basket-thumbs img:visible:first");

            function scroll_left() {
                if (first.position().top <= first_row_top && $("#basket-thumbs img:hidden:last").show().length == 1)
                    setTimeout(scroll_left, 20);
                else
                    basket_scroll_arrows();
            }

            scroll_left();
        }
    });

    $("#basket-thumbs img").live('mouseover', function (event) {
        var $this = $(this);
        $("#basket-unselect").remove();
        var b = $("<input type='checkbox' id='basket-unselect' checked='checked' style='position: absolute; z-index: 1000;'>");
        b.appendTo($("#basket-thumbs")).offset($this.offset()).click(function () {
            var id = $($this).attr("id");
            id = id.substring(id.lastIndexOf('-') + 1);
            recordSelection(id, false);
        });
    });
    $("#basket-thumbs").bind('mouseleave', function (event) {
        $("#basket-unselect").remove();
    });

    basket_scroll_arrows();

    bindSelectRecordCheckboxes();

    // drag and drop records to basket

    $("#basket-content").droppable({
        accept: "#content-wrapper .record-anchor[id*=record-id-]",
        activeClass: "dragging",
        hoverClass: "hovering",
        drop: function (event, ui) {
            var id = ui.draggable.attr("id");
            id = id.substring(id.lastIndexOf('-') + 1);
            recordSelection(id, true);
            ui.draggable.parents(".record").find("input.record-select").attr('checked', true);
        },
        activate: function (event, ui) {
            ui.helper.css('z-index', '10001');
        }
    });

    keepAtTop($("#basket-content"));


    $("#content-wrapper .record-anchor[id^=record-id-]").draggable({
        containment: 'window',
        helper: 'clone',
        appendTo: 'body',
        scroll: false
    });

    // end basket features

    if (!custom_process_facets) process_facets();
    $(".autocomplete-user").autocomplete('{% url 'api-autocomplete-user' %}', {});
    $(".autocomplete-group").autocomplete('{% url 'api-autocomplete-group' %}', {});
    $(".impersonation-autocomplete").autocomplete('{% url 'impersonation-autocomplete-user' %}', {});

    setTimeout(function () {
        $("#messages").css('visibility', 'hidden');
    }, 8000);

    // convert list of actions to row drop-down menu
    $("table.itemactions tr+tr").each(function () {
        var r = $(this);
        var c = $("<td class='item-actions-menu'><img src='{% static 'images/down_arrow.png' %}' /><" + "/td>");
        var u = $("<ul><" + "/ul>");
        $("td.item-actions a, td.item-actions input", r).each(function () {
            var item = $(this);
            if (!item.hasClass('item-action-important')) {
                var li = $("<li><" + "/li>").append(item);
                u.append(li);
            }
            addCopyLinkIcon(item);
        });
        if (!u.children().length) u.append($("<li>No actions available<" + "/li>"));
        r.append(c.append($("<div><" + "/div>").append(u)));
    });

    $(document).click(function () {
        $("table.itemactions tr.actionrow-open").removeClass('actionrow-open');
    });

    $("table.itemactions tr+tr a, table.itemactions tr+tr input").click(function (event) {
        event.stopPropagation();
    });

    $("table.itemactions tr+tr").mouseenter(function () {
        $("table.itemactions tr.actionrow-selected").removeClass("actionrow-selected");
        $(this).addClass("actionrow-selected");
    }).click(function () {
        var r = $(this);
        if (r.hasClass('actionrow-open')) return;

        $("table.itemactions tr.actionrow-open").removeClass('actionrow-open');

        r.addClass('actionrow-open');
        var menu = $("td.item-actions-menu div", r)
        var o = {
            left: r.offset().left + r.width() - menu.width() - 1,
            top: r.offset().top + r.height() - 1
        };
        // apply offset twice, first time around does not always work on Chrome
        menu.offset(o);
        menu.offset(o);
        return false;
    });


    // actionbar functions

    $(document).click(function () {
        $("ul.actionbar li div.dropdown").hide();
    });
    $("ul.actionbar li div.dropdown").click(function (event) {
        event.stopPropagation();
    }).each(function () {
        var d = $(".dropdown-anchor", $(this).parent());
        d.click(function () {
            var r = $(this).parent();
            var menu = $("div.dropdown", r);
            if (menu.is(":visible")) {
                menu.hide();
            } else {
                // hide all other menus
                $("ul.actionbar li div.dropdown").hide();
                var o = {
                    left: r.offset().left - 1,
                    top: r.offset().top + 28
                };
                // apply offset twice, first time around does not always work on Chrome
                menu.show();
                menu.offset(o);
                menu.offset(o);
                menu.trigger('actionbar-dropdown-open');
            }
            return false;
        });
    }).css("cursor", "default");

    $("ul.actionbar li div.tags-dropdown").bind('actionbar-dropdown-open', function () {
        var menu = $(this);
        var tags = {};
        var rows = 0;
        // get selected rows and count different tags
        $("input:checkbox:checked[name=h]").each(function () {
            var row = $(this).parent().parent();
            $("span.tag span.t", row).each(function () {
                var t = $(this).text();
                tags[t] = (tags[t] || 0) + 1;
            });
            rows++;
        });
        if (rows) $("input:checkbox", menu).each(function () {
            var t = $(this).next().text();
            var c = $("<input type='checkbox' value='true' />");
            c.attr('name', $(this).attr('name'));
            if (tags[t]) {
                if (tags[t] == rows) {
                    c.attr('checked', 'checked');
                } else {
                    c.multicheckbox({'mixed': true});
                }
            } else {
                c.attr('checked', '');
            }
            $(this).replaceWith(c);
        });
    });
});
