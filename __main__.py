from multiprocessing import cpu_count

from uvicorn import run

from configs.envs import DEBUG, HOST, LOG_LEVEL, PORT

if __name__ == '__main__':
    run('app:create_app',
        host=HOST,
        port=PORT,
        log_level=LOG_LEVEL.lower(),
        reload=DEBUG,
        workers=cpu_count(),
        factory=True)
