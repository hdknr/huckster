# Accounts 

## User and Application

- An [User](/admin/auth/user/) is created when he has signed up.
- An [Application](/admin/oauth2_provider/application/) is created for this User.

    - `Client Type` is `Public`
    - `Authorization grant type` is [Client credentials](https://tools.ietf.org/html/rfc6749#section-4.4)

## Players' credentials

- User gives `client_id` and `client_secret` to a signage player which aquires an access token from the server.
- Players keep access token in some secure manner. (Key Chain)

OS:

- macOS: [Key Chain](https://support.apple.com/kb/PH25230?viewlocale=ja_JP&locale=ja_JP)
- Widnows: [Windows Credential Manager](https://support.microsoft.com/ja-jp/help/4026814/windows-accessing-credential-manager)
- Linux: [Secret Service API](https://specifications.freedesktop.org/secret-service/), [libsecret](https://wiki.gnome.org/Projects/Libsecret)