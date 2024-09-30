from pydantic import BaseModel, ConfigDict


class RedisDataSchema(BaseModel):
    message: str
    phone: str
    pay_link: str

    model_config = ConfigDict(from_attributes=True)


class RedisMessageStruct:
    def __init__(
            self, key: bytes | str, value: bytes | str, phone: bytes | str, pay_link: bytes | str, project: bytes | str
    ) -> None:
        self.__key = key.decode('utf-8')
        self.__value = value.decode('utf-8')
        self.__phone = phone.decode('utf-8')
        self.__pay_link = pay_link.decode('utf-8')
        self.__project = project.decode('utf-8')

    def data(self) -> dict[str, str]:
        return {
            'key': self.__key,
            'message': self.__value,
            'phone': self.__phone,
            'pay_link': self.__pay_link,
            'project': self.__project
        }
