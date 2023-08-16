from pymysqlpool import ConnectionPool


class ConnectionPoolSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = cls._create_pool(*args, **kwargs)

        return cls._instance

    @staticmethod
    def _create_pool(*args, **kwargs):
        return ConnectionPool(*args, **kwargs)
