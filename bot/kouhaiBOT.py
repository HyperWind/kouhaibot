

import ch
import time
from random import randint
import random
import sys
import re
if sys.version_info[0] > 2:
  import urllib.request as urlreq
else:
  import urllib2 as urlreq


killme = [
  "Stabs @ in the eye.",
  "Bites @ 's arm off.",
  "Goes full on tsundere on @ .",
  "Shoots an arrow in @ 's knee.",
  "Shoots @ in the foot.",
  "Makes a hamburger out of @ .",
  "Makes @ learn C++.",
  "Eats @ 's heart."
]

dancemoves = [
  "(>^.^)>",
  "(v^.^)v",
  "v(^.^v)",
  "<(^.^<)"
]

flips = [
  "Hits her head.",
  "Slips and falls down.",
  "Fails and makes a baka out of herself.",
  "Sneezes and falls down.",
  "Actually pulls off the flip.",
  "Accidentally hits someone with her leg.",
  "Makes a #JeanFail.",
  "Gets ebola.",
  "Falls down the stairs."
]

sempai = [
  "blushes",
  "passes out",
  "goes full on fujoshi",
  "freaks out",
  "does nothing",
  "writes a yaoi fanfic about that"
]

yandere = [
  " Oh @ where are you?",
  " @ , come out~!",
  " @ , I want to play with you...",
  " You are the only one I love @ .",
  " I want only you @ .",
  " My love for you is infinate @ .",
  " Please, why don't you love me @ ?"
]

tsundere = [
  " Baka! @",
  " It's not like I like you or anything @ ...",
  " Hmpf... @",
  " I hate you @ !",
  " Get away @ !",
  " Piss off @ !",
  " I don't like you @ !"
]

insults = [
  " @ smells like poo.",
  " If @ was in an eroge, their face would be censored.",
  " I would rather eat a bug than look at @ 's face.",
  " Even Kirito-kun wouldn't accept @ into his harem.",
  " I once saw @ 's face, now I'm blind.",
  " @ is a baka gaijin!",
  " @ is so boring that I'd rather watch Vampire Knight than talk to them.",
  " @ 's mama is so fat, she even has her own gravity field.",
  " Captain Earth makes more sense than @.",
  " @ enjoyed Boku no Pico way too much.",
  " @ has such shit taste that they have Mars of Destruction on their favorites list."
]

lewd = [
  " S-sempai, what are you doing? Why are you holding me like that?",
  " No, s-sempai, please, s-stop...No, d-don't remove that s-sempai...",
  " What are you doing s-sempai, why are you putting it in there?",
  " S-SEMPAI!!! HNNNNNNGGGG!! S-ssem-mpai..."
]

last_time = 0

class kouhai_bot(ch.RoomManager):
  def onInit(self):
    self.setNameColor("F9F")
    self.setFontColor("F33")
    self.setFontFace("1")
    self.setFontSize(13)
    self.enableBg()
    self.enableRecording()

  def onConnect(self, room):
    print("Connected")
    room.message("Minna, konnichiwa!")

  def onReconnect(self, room):
    print("Reconnected")

  def onDisconnect(self, room):
    print("Disconnected")

  def onMessage(self, room, user, message):

    long_c = 0

    if room.getLevel(self.user) > 0:
      print(user.name, message.body)
    else:
      print(user.name, message.body)

    if self.user == user: return

    global last_time

    print(time.time(), " ", last_time, " ", time.time() - last_time)
    if (message.body[0] == "/" and time.time() - last_time > 2):   ##Here is the Prefix part
      data = message.body[1:].split(" ", 1)
      if len(data) > 1:
        cmd, args = data[0], data[1]
      else:
        cmd, args = data[0], ""

      if cmd == "say":
        room.message(args)

      elif cmd == "scrub":
        room.message( "@" + random.choice(room.usernames) + " is a scrub.")

      elif cmd == "mods":
        modlist = " ".join(room.modnames + [room.ownername])
        room.message("Online mods:" + modlist)

      elif cmd == "users":
        userlist= " ".join(room.usernames)
        room.message("Online users: " + userlist)

      elif cmd == "dance":
        last_time = time.time() + 8
        long_c = 1
        for i, msg in enumerate(dancemoves):
          self.setTimeout(i * 2, room.message, msg)

      elif cmd == "lewd":
        last_time = time.time() + 8
        long_c = 1
        for i, msg in enumerate(lewd):
          self.setTimeout(i * 2, room.message, msg)

      elif cmd == "insult":
        response = insults[randint(0, len(insults)-1)].split("@")
        room.message(response[0] + args + response[1])

      elif cmd == "flip":
        room.message("*does a flip*")
        self.setTimeout(2, room.message, "*" + flips[randint(0, len(flips)-1)] + "*")

      elif cmd == "baka":
        room.message(" No, you are @" + user.name + " .")

      elif cmd == "intro":
        room.message(" Konnichiwa! Watashi wa KouhaiBOT (v1.0) desu. And I'm a chatango chat bot!")

      elif cmd == "true?":
        if randint(0, 1) == 0:
          room.message(" Yes, it's true...")
        else:
          room.message(" No, that's not true at all!")

      elif cmd == "yandere":
        response = yandere[randint(0, len(yandere)-1)].split("@")
        room.message(" http://i.imgur.com/0FCWZSQ.png " + response[0] + args + response[1])

      elif cmd == "tsundere":
        response = tsundere[randint(0, len(tsundere)-1)].split("@")
        room.message(" http://i.imgur.com/UZmxhc4.png " + response[0] + args + response[1])

      elif cmd == "weeaboo":
        room.message(" https://www.youtube.com/watch?v=TBfWKmRFTjM This song discribes you pretty accurately " + args + " .")

      elif cmd == "commands":
        room.message("> /commands, /cookie, /weeaboo (arg), /rape (arg), /users, /tsundere (arg), /kill (arg), /notice, /yandere (arg), /true? (arg), /intro, /flip, /insult (arg), /baka, /lewd, /dance, /roulette, /scrub, /mods. <")

      elif cmd == "roulette":
        if randint(1, 100) < 25:
          room.message("@" + user.name + " makes a hole in their head, better luck next time.")
        else:
          room.message("@" + user.name + " shoots an empty round, that was close.")

      elif cmd == "notice":
        room.message("@" + user.name + " sempai notices @kouhaiBOT.")
        self.setTimeout(2, room.message, "*@kouhaiBOT " + sempai[randint(0, len(sempai)-1)] + "*")

      elif cmd == "cookie":
        room.message("Thanks @" + user.name + " sempai, that was delicious.")

      elif cmd == "kill":
        response = killme[randint(0, len(killme)-1)].split("@")
        room.message("*" + response[0] + args + response[1] + "*")

      elif cmd == "rape":
        room.message("Come here " + args + " !")
        self.setTimeout(2, room.message, "*Rapes " + args + " .*")

      else:
        room.message("I don't know that command!")

      if long_c != 1: last_time = time.time()
      else: long_c = 0;

  def onFloodWarning(self, room):
    room.reconnect()

  def onJoin(self, room, user):
   print(user.name + " joined the chat!")

  def onLeave(self, room, user):
   print(user.name + " left the chat!")

  def onUserCountChange(self, room):
    print("users: " + str(room.usercount))

  def onMessageDelete(self, room, user, msg):
    print("MESSAGE DELETED: " + user.name + ": " + msg.body)


if __name__ == "__main__": kouhai_bot.easy_start()
