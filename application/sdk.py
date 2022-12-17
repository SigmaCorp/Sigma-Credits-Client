import aiohttp
import json
from typing import Any, ClassVar, Dict


class Route:
    BASE: ClassVar[str] = "https://sigma-search.io/api/sigma"

    def __init__(self, method: str, path: str):
        self.method = method
        self.path = path

    @property
    def url(self) -> str:
        return f"{self.BASE}{self.path}"


class SigmaCreditSDK:
    def __init__(self, token: str):
        self.token = token

    async def request(self, route: Route, **kwargs: Any) -> Any:
        url = route.url
        method = route.method

        headers: Dict[str, str] = {
            "User-Agent": "Sigma Credits Client - Integrated SDK v1.0",
            "sigma-key": self.token,
        }

        if "json" in kwargs:
            headers["Content-Type"] = "application/json"
            kwargs["data"] = json.dumps(kwargs.pop("json"))

        kwargs["headers"] = headers

        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, **kwargs) as response:
                if "application/json" in response.headers["content-type"]:
                    rcontent = await response.json()
                else:
                    rcontent = await response.text()

        return rcontent

    def balance(self):
        return self.request(
            Route("POST", "/creditos"), json={"token": self.token}
        )

    def search_dni(self, dni: str, gender: str):
        data = {
            "metodo": "buscar_dni",
            "args": {
                "dni": dni,
                "sexo": gender,
            },
        }
        return self.request(Route("POST", "/sigma_credits"), json=data)

    def search_plate(self, plate: str):
        data = {
            "metodo": "buscar_patentes",
            "args": {"patente": plate},
        }
        return self.request(Route("POST", "/sigma_credits"), json=data)

    def search_phone(self, phone: str):
        data = {
            "metodo": "buscar_celular",
            "args": {"numero": phone},
        }
        return self.request(Route("POST", "/sigma_credits"), json=data)

    def search_name(
        self,
        name: str,
        province: int = -1,
        city: str = "",
        minage: int = 0,
        maxage: int = 0,
    ):
        args = {"nombre": name}

        if province >= 0:
            args["provincia_id"] = province

        if city:
            args["localidad"] = city

        if minage:
            args["edad_desde"] = minage

        if maxage:
            args["edad_hasta"] = maxage

        data = {
            "metodo": "buscar_nombre",
            "args": args,
        }
        return self.request(Route("POST", "/sigma_credits"), json=data)

    def search_address(self, address: str):
        data = {
            "metodo": "buscar_direccion",
            "args": {"direccion": address},
        }
        return self.request(Route("POST", "/sigma_credits"), json=data)

    def search_email(self, email: str):
        data = {
            "metodo": "buscar_datos",
            "args": {"tipo": "buscar_email", "dato": email},
        }
        return self.request(Route("POST", "/sigma_credits"), json=data)

    def search_number(self, number: str):
        data = {
            "metodo": "buscar_datos",
            "args": {"tipo": "buscar_celular", "dato": number},
        }
        return self.request(Route("POST", "/sigma_credits"), json=data)

    def search_cbu(self, cbu_alias: str):
        data = {
            "metodo": "buscar_datos",
            "args": {"tipo": "buscar_cbu_alias", "dato": cbu_alias},
        }
        return self.request(Route("POST", "/sigma_credits"), json=data)

    def search_breach(self, query: str):
        data = {
            "metodo": "buscar_breach",
            "args": {"query": query},
        }
        return self.request(Route("POST", "/sigma_credits"), json=data)

    @classmethod
    async def from_login(cls, username: str, password: str):
        sdk = cls("")
        res = await sdk.request(
            Route("POST", "/client/login"),
            json={"username": username, "password": password},
        )
        sdk.token = res["token"]
        return sdk


async def testing():
    sclient = await SigmaCreditSDK.from_login("notcia", "barto1337@!L")
    results = await sclient.balance()
    print(results)


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(testing())
