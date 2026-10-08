# ratio

A small script that compares your Instagram followers with the accounts you follow. It tells you:

1. **Who doesn't follow you back:** accounts you follow that don't follow you.
2. **Who you don't follow back:** accounts that follow you that you don't follow.

It runs on your own computer and only reads the files you give it. Nothing is sent anywhere.

## What you need

- **Python 3.** Macs usually have it already. To check, open the Terminal app and type:

  ```
  python3 --version
  ```

  If you see something like `Python 3.12.1`, you're set. If not, install it from [python.org](https://www.python.org/downloads/).
- **Your Instagram data download.** See the next section.

## Step 1: Download your Instagram data

1. In the Instagram app or website, go to **Settings → Accounts Center → Your information and permissions → Download your information**.
2. Request a download. You can pick just **Followers and following** to make it smaller.
3. Choose the **HTML** format. JSON works too.
4. Instagram emails you when it's ready, which can take minutes or hours. Download the zip and unzip it.

Inside the unzipped folder, go to:

```
connections/followers_and_following/
```

The two files you need are:

| File | What it contains |
|---|---|
| `followers_1.html` | Everyone who follows you |
| `following.html` | Everyone you follow |

If you have a lot of followers, there may also be `followers_2.html`, `followers_3.html` and so on.

## Step 2: Run the script

Open Terminal and go to the folder that contains `ratio.py`:

```
cd ~/ratio
```

Then run:

```
python3 ratio.py FOLLOWERS_FILE FOLLOWING_FILE
```

The followers file goes first and the following file goes second.

**Tip:** you don't have to type the long file paths. Type `python3 ratio.py ` (with a space at the end), then drag `followers_1.html` from Finder into the Terminal window. Type another space and drag in `following.html`. Then press Enter.

A full example:

```
python3 ratio.py ~/Downloads/instagram-yourname-2026-10-08/connections/followers_and_following/followers_1.html ~/Downloads/instagram-yourname-2026-10-08/connections/followers_and_following/following.html
```

**More than one followers file?** List them all, separated by commas with no spaces, as the first argument:

```
python3 ratio.py followers_1.html,followers_2.html following.html
```

## What you'll see

The output looks like this (these are made-up names):

```
Followers: 610   Following: 656

Don't follow you back (you follow them) (3)
-------------------------------------------
  coffee_shop_daily  https://www.instagram.com/coffee_shop_daily
  famous_person  https://www.instagram.com/famous_person
  old_classmate  https://www.instagram.com/old_classmate

You don't follow back (they follow you) (1)
-------------------------------------------
  new_friend_22  https://www.instagram.com/new_friend_22
```

- The first line shows how many followers and following the script found. These numbers should match what your Instagram profile showed on the day you downloaded the data.
- Each list is in alphabetical order. The number in parentheses is how many people are in that list.
- Each name comes with a link to that person's profile. In most terminals you can Cmd-click the link to open it.

**Saving the results to a file:** add `> results.txt` to the end of the command. The output goes into `results.txt` instead of the screen.

## Common problems

| Problem | Fix |
|---|---|
| `No such file or directory` | The file path is wrong. Drag the file into Terminal instead of typing the path. |
| It prints the usage message instead of results | You need exactly two file arguments: followers first, following second. |
| The counts look too low | Make sure you included every `followers_N.html` file, separated by commas. |
| The lists look backwards | You probably swapped the files. Followers goes first. |

## Good to know

- **The results are only as fresh as your download.** If someone followed or unfollowed you after you downloaded your data, the script won't know. Download your data again to get updated results.
- **Uppercase and lowercase don't matter.** `CoolUser` and `cooluser` count as the same person.
- **Accounts that are deactivated or changed their username** may show up in the lists, because the download keeps the old name.
