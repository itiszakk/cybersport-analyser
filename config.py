import os

tempPath = os.path.abspath("temp")
softPath = os.path.abspath("vendor")
inputPath = os.path.abspath("input")

databasePath = r"{}\database".format(tempPath)
logsPath = r"{}\logs".format(tempPath)

games = ["counterstrike", "dota2", "leagueoflegends", "valorant"]

databaseName = "database"
userName = "analyser"

batchSize = 100