from pydantic import BaseModel, ConfigDict


class RedisDataSchema(BaseModel):
    message: str
    phone: str
    pay_link: str

    model_config = ConfigDict(from_attributes=True)


class RedisMessageStruct:
    def __init__(self, key, value, phone, pay_link, project) -> None:
        self.key = key.decode('utf-8')
        self.value = value.decode('utf-8')
        self.phone = phone.decode('utf-8')
        self.pay_link = pay_link.decode('utf-8')
        self.project = project.decode('utf-8')

    def data(self) -> dict[str, str]:
        return {
            'key': self.key,
            'message': self.value,
            'phone': self.phone,
            'pay_link': self.pay_link,
            'project': self.project
        }
