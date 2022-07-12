# Roblox IP Bot - Python | Napalm

## Setup
Open `config.json` and sort everything out. It's all straight forwards besides `roles`.

Pretty much you can only run the specified command if you have a role matching the value you give it. For example.

```json
{
    "roles": {
        "plr": "plr_whitelist"
    }
}
```
Now to run the `plr` command on the bot you must have a role which is named `plr_whitelist`. You can give multiple/all commands the same whitelist role name.

Another thing to setup is the bot's activity. Navigate yourself to `main.py` and find the variable `activity`. Edit this how you want.

The second last thing to setup is your method for hitting roblox servers when using the `kill` command. Navigate to `main.py` and edit the `kill_method` variable correctly

The last thing to setup is your booter api url. Navigate to `main.py` and edit it. If you do not understand how `.format` works in the way I used it, message me @ nathan#2400


## Tips
To disable a command navigate to `main.py` and comment out the `bot.load_extension()` line with ur command in it. For example
```python
bot.load_extension("Cogs.Commands.Plr")
# bot.load_extension("Cogs.Commands.Universe")
```
You just disabled the `universe` command by commenting it out.
