import configparser

config = configparser.ConfigParser()
config_file_path = r"C:/Users/maheshpriya.j/PycharmProjects/Automation_NasbaStore/Configuration/config.ini"
config.read(config_file_path)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

