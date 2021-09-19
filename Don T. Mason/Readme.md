# H@cktivityCon: Don T. Mason
 
![warmup category](https://img.shields.io/badge/Category-OSINT-brightgreen.svg)  
![score](https://img.shields.io/badge/Score_after_CTF-482-blue.svg)  
![solves](https://img.shields.io/badge/Solves-42-lightgrey.svg) 

## Description
So this is a weird one. We've been having trouble tracking down Don because of the name conflict between some baseball player or something? All we know is that he likes elephants. Like, he reaalllyy likes elephants.

## Attached files
- None
## Summary
He is on https://mastodon.social/@donmason

## Flag
```
flag{fbec1486e542c5d96f725cd6009ffef5}
```

## Detailed solution
I used this tool (https://github.com/sherlock-project/sherlock) to find all pages with the username ```donmason```.
```
$ python3 sherlock donmason
[*] Checking username donmason on:
[+] 9GAG: https://www.9gag.com/u/donmason
[+] AskFM: https://ask.fm/donmason
[+] Bandcamp: https://www.bandcamp.com/donmason
[+] Blogger: https://donmason.blogspot.com
[+] Bookcrossing: https://www.bookcrossing.com/mybookshelf/donmason/
[+] Codecademy: https://www.codecademy.com/profiles/donmason
[+] Coroflot: https://www.coroflot.com/donmason
[+] DeviantART: https://donmason.deviantart.com
[+] Disqus: https://disqus.com/donmason
[+] Duolingo: https://www.duolingo.com/profile/donmason
[+] Ello: https://ello.co/donmason
[+] Euw: https://euw.op.gg/summoner/userName=donmason
[+] Facebook: https://www.facebook.com/donmason
[+] Flickr: https://www.flickr.com/people/donmason
[+] Flipboard: https://flipboard.com/@donmason
[+] FortniteTracker: https://fortnitetracker.com/profile/all/donmason
[+] Freelancer: https://www.freelancer.com/u/donmason
[+] Houzz: https://houzz.com/user/donmason
[+] HubPages: https://hubpages.com/@donmason
[+] IFTTT: https://www.ifttt.com/p/donmason
[+] Issuu: https://issuu.com/donmason
[+] Kik: https://kik.me/donmason
[+] Kongregate: https://www.kongregate.com/accounts/donmason
[+] Medium: https://medium.com/@donmason
[+] Myspace: https://myspace.com/donmason
[+] Periscope: https://www.periscope.tv/donmason/
[+] Pinterest: https://www.pinterest.com/donmason/
[+] Quizlet: https://quizlet.com/donmason
[+] Redbubble: https://www.redbubble.com/people/donmason
[+] Reddit: https://www.reddit.com/user/donmason
[+] Roblox: https://www.roblox.com/user.aspx?username=donmason
[+] SlideShare: https://slideshare.net/donmason
[+] Smule: https://www.smule.com/donmason
[+] Spotify: https://open.spotify.com/user/donmason
[+] Telegram: https://t.me/donmason
[+] TikTok: https://tiktok.com/@donmason
[+] TrackmaniaLadder: http://en.tm-ladder.com/donmason_rech.php
[+] TradingView: https://www.tradingview.com/u/donmason/
[+] Trakt: https://www.trakt.tv/users/donmason
[+] Trello: https://trello.com/donmason
[+] Twitch: https://www.twitch.tv/donmason
[+] VK: https://vk.com/donmason
[+] VSCO: https://vsco.co/donmason
[+] Venmo: https://venmo.com/donmason
[+] Warrior Forum: https://www.warriorforum.com/members/donmason.html
[+] Wattpad: https://www.wattpad.com/user/donmason
[+] Windy: https://community.windy.com/user/donmason
[+] WordPress: https://donmason.wordpress.com/
[+] WordPressOrg: https://profiles.wordpress.org/donmason/
[+] Xbox Gamertag: https://xboxgamertag.com/search/donmason
[+] YouNow: https://www.younow.com/donmason/
[+] forum_guns: https://forum.guns.ru/forummisc/blog/donmason
[+] last.fm: https://last.fm/user/donmason
[+] mastodon.social: https://mastodon.social/@donmason
[+] osu!: https://osu.ppy.sh/users/donmason
```

I manually checked every page with one clue in mind: **```elephant```**  
After a while, I found him on https://mastodon.social/@donmason  
I scrolled through 2 pages of elephant loving posts and found the one with the flag:  
https://mastodon.social/@donmason?max_id=106774436605922101 (the user may not be available after CTF)
<p align="center">
  <img src="https://user-images.githubusercontent.com/55624202/133942344-385db133-35e0-4cc0-8c39-d827b9dbdfde.png" />
</p>
  
The flag is:
```
flag{fbec1486e542c5d96f725cd6009ffef5}
```
