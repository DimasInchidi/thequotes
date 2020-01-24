```
           :::                 :::::::
    :+:   :+:                :+:    :+:                   :+:
   +:+   +:+       +:+:+    +:+    +:+ +:+  +:+  +:++:+  +:+    +:+:+   +:+:+
  +#+++ +#+::+   +#  +#+   +#+    +:+ +#+  +:+ +#+  +:+ +#+++ +#  +#+ +:
 +#+   +#+ ++#+ +#####+   +#+ ++ +#+ +#+  +#+ +#+  +#+ +#+   +#####+   +##+
#+#   #+#  #+# #+        #+#   ##+# #+#  #+# #+#  #+# #+#   #+            +#
#### ###  ###   ####      #########  #### ##  ####    ####   ####    #####
```

# Running

- Run `pip --user -r requirements.txt` to install requirements.
- Create `.env` based from `.env.example` with your values.
- Make sure your bot isn't running on [privacy mode](https://core.telegram.org/bots#privacy-mode).
- Run `python main.py` to start the daemon.

# Usage
- Add this bot to your channel.
- Reply message with `/add` to add quotes, the bot would reply with quote id.
- Send `/get x` with `x` as quote id to recall specific quote.
- Send `/random` to recall random quote.
- Send `/remove x` with `x` as quote id to remove quote from database.
