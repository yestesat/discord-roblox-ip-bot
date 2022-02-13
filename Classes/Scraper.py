import aiohttp
import json


with open("./config.json", "r") as r:
    cookie = json.load(r)["roblox"]["cookie"]


class Scraper():

    def __init__(self, placeid):
        self.placeid = placeid
        self.cookies = {
            ".ROBLOSECURITY": cookie
        }
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "Referer": "https://www.roblox.com/games/",
            "Origin": "https://www.roblox.com/",
        }
        self.join_script_headers = {
            'User-Agent': 'User-Agent: Roblox/WinInet'
        }


    async def get(self, url: str, headers: dict):
        async with aiohttp.ClientSession(cookies=self.cookies) as s:
            async with s.get(url, headers=headers) as res:
                return await res.json()



    async def post(self, url: str, headers: dict, join_script: bool = False):
        async with aiohttp.ClientSession(cookies=self.cookies) as s:
            async with s.post(url, headers=headers) as res:
                if join_script == False:
                    return await res.json()

                return await res.text()


    def set_placeid(self, placeid: str):
        self.placeid = placeid


    async def get_information(self):
        gamev1 = await self.get(
            f"https://games.roblox.com/v1/games/{self.placeid}/servers/Public?sortOrder=Asc&limit=25",
            self.headers
        )
        data = gamev1["data"]
        pack = []

        for i,_ in enumerate(data):
            if data[i]["maxPlayers"] == 1 or data[i]["maxPlayers"] == data[i]["playing"]:
                continue

            server_id = data[i]["id"]
            information = await self.post(
                f"https://assetgame.roblox.com/Game/PlaceLauncher.ashx?request=RequestGameJob&placeId={self.placeid}&gameId={server_id}",
                self.headers
            )
            join_script_url = information["joinScriptUrl"]

            if join_script_url == None:
                continue

            jsr = await self.post(
                join_script_url,
                self.headers,
                True
            )
            server_information = json.loads(jsr.split("==%")[1])

            pack.append(
                {
                    "ip": server_information["MachineAddress"],
                    "port": server_information["ServerPort"],
                    "players": data[i]["playing"],
                    "ping": data[i]["ping"],
                    "maxPlayers": data[i]["maxPlayers"]
                }
            )

        title = await self.get(
            f"https://games.roblox.com/v1/games/multiget-place-details?placeids={self.placeid}",
            self.headers
        )
        title = title[0]["name"]

        return {
            "package": pack,
            "title": title
        }
 