import os.path

install_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
localcss = os.path.join(install_dir, 'templates_local', 'local.css')
localjs =  os.path.join(install_dir, 'templates_local', 'local.js')

def local_static(context):
    return {
        'LOCAL_CSS': localcss if os.path.exists(localcss) else False,
        'LOCAL_JS':  localjs  if os.path.exists(localjs)  else False,
        }


