import positron

positron.main_level = positron.LogLevel.DEBUG
log = positron.Logger('log', positron.LogLevel.IMPORTANT)
log.enable_file_logging()
log.debug('debug')
log.io('io')
log.info('info')
log.warning('warning')
log.error('error')
log.important('important')
log.critical('critical')
log.iochars = 'MSG'
log.io('msg')