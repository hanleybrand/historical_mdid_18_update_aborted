import logging

from rooibos.solr import SolrIndex
from rooibos.workers.registration import register_worker, run_worker


log = logging.getLogger(__name__)


@register_worker("solr_index")
def solr_index(data):
    log.info("Starting solr index")
    count = SolrIndex().index()
    log.info("solr index done, indexed %d records" % count)


def schedule_solr_index():
    run_worker("solr_index", None)
