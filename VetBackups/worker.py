import shutil
import datetime
import logger
import os
import tarfile
import win32serviceutil

srcpath = 'c:\\Install'
now = datetime.datetime.now().strftime("%m%d%Y_%H%M%S")
dstpath = 'c:\\backups\\{0}'.format(now)
tarExt = '.gz'
tarType = 'w:gz'
servicename = 'TeamViewer'
log = logger.get_logger(name='FabricLogger', path_for_log='c:\\temp', file_name='vetbackups.log')

def service_info(action, service):

    if action == 'stop':
        win32serviceutil.StopService(service)
        log.info('service={0} action=stopped result=successfully'.format(service))
    elif action == 'start':
        win32serviceutil.StartService(service)
        log.info('service={0} action=started result=successfully'.format(service))
    elif action == 'restart':
        win32serviceutil.RestartService(service)
        long.info('service={0} action=restarted result=successfully'.format(service))
    elif action == 'status':
        if win32serviceutil.QueryServiceStatus(service)[1] == 4:
            log.info('service={0} status=running'.format(service))
            return 'running'
        else:
            log.info('service={0} status="*not* running"'.format(service))
            return 'notrunning'

def do_copy():
    '''Copies files/folders'''

    try:
        log_line = 'foldertocopy="{0} backupdest="{1}'.format(srcpath,dstpath)
        log.info(log_line)
        shutil.copytree(srcpath,dstpath)
        make_tarfile(dstpath)
    except Exception as ex:
        template = "An exception of type {0} has occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)

        log.info(message)

def make_tarfile(tarpath):
    '''Creates a tarball from provided path'''

    try:
        log_line = 'tarfilename="{0} function=make_tarfile'.format(tarpath,tarExt)
        log.info(log_line)
        archivename = '{0}{1}'.format(tarpath, tarExt)
        archive = tarfile.open(archivename, tarType)
        archive.add(tarpath, arcname=os.path.basename(tarpath))
    except Exception as ex:
        template = "An exception of type {0} has occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)

        log.info(message)


def main():
    out = service_info('status',servicename)
    if out == "notrunning":
        service_info('start',servicename)
    #do_copy()

if __name__ == '__main__':
    main()