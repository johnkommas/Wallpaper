def main_body(store_name, retail_point, complete_time):
    date, time = complete_time.split(" ")
    html_start = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
"""
    html_head = """
    <head>
    <!--[if gte mso 9]><xml> <o:OfficeDocumentSettings> <o:AllowPNG/> <o:PixelsPerInch>96</o:PixelsPerInch> </o:OfficeDocumentSettings> </xml><![endif]-->
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <meta name="HandheldFriendly" content="true"/>
    <meta name="MobileOptimized" content="320"/>
    <meta name="viewport" content="width=device-width"/>
    <meta name="color-scheme" content="light only">
    <meta name="supported-color-schemes" content="light only">
    <title></title>
    <!--[if !mso]><!-->
    <link href="https://www.cdn1ve3zg.com/shared/fonts/SuisseIntlMono/stylesheet.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&amp;display=swap" rel="stylesheet" type="text/css">
    <link href="https://www.cdn1ve3zg.com/shared/fonts/Apercu/stylesheet.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css2?family=Work+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&amp;display=swap" rel="stylesheet" type="text/css">
    <!--<![endif]-->
    <style type="text/css">
    #MessageViewBody a {
        color: inherit;
        text-decoration: none;
        font-size: inherit;
        font-family: inherit;
        font-weight: inherit;
        line-height: inherit
    }

    [data-outlook-cycle] [x-apple-data-detectors-type="calendar-event"] {
        color: inherit !important;
        -webkit-text-decoration-color: inherit !important;
        text-decoration:none !important
    }

    span, td, table, div {
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing:grayscale
    }

    .st-email-body {
        width: 100% !important;
        -webkit-text-size-adjust: 100%;
        margin: 0 auto !important;
        padding: 0;
        background-color:#fff
    }

    span.st-preheader {
        display:none !important
    }

    img + div {
        display: none
    }

    a[href^="tel"], a[href^="sms"] {
        text-decoration: none;
        color: inherit !important;
        pointer-events: none;
        cursor:default
    }

    u + .st-email-body a {
        color: inherit;
        text-decoration: none;
        font-size: inherit;
        font-family: inherit;
        font-weight: inherit;
        line-height:inherit
    }

    * [x-apple-data-detectors] {
        color: inherit !important;
        text-decoration: none !important;
        font-size: inherit !important;
        font-family: inherit !important;
        font-weight: inherit !important;
        line-height:inherit !important
    }

    a, a:hover, a:link, a:visited {
        text-decoration: none !important;
        outline:0
    }

    p {
        margin: 0;
        padding:0
    }

    .st-hide-desktop {
        display: none;
        font-size: 0;
        height: 0;
        min-height: 0;
        max-height: 0;
        line-height: 0;
        mso-hide:all
    }

    .st-gmail-fix {
        display:none !important
    }

    @media screen and (max-width: 480px) {
        .st-col, .st-mobile-full-width, .st-module-wrapper-table, .st-wrapper, .st-wrapper-table {
            width:100% !important
        }

        .st-col {
            padding:0 !important
        }

        .st-resize {
            width:100% !important
        }

        .st-mobile-width-constraint, .st-resize {
            display: block !important;
            height:auto !important
        }

        .st-mobile-width-constraint {
            max-width:100% !important
        }

        .st-equal-height, .st-height-auto {
            height:auto !important
        }

        .st-hide-desktop {
            display:table-row !important
        }

        .st-hide-mobile {
            display:none !important
        }

        .st-mobile-inline {
            display:inline !important
        }

        .show-img-mobile {
            display: table-row !important;
            width: 100% !important;
            float: none;
            overflow: visible !important;
            height:auto !important
        }

        .st-dynamic-999-2, u + .st-email-body .st-dynamic-999-2 img {
            width: 100% !important;
            max-width:102px !important
        }

        .st-dynamic-981-5 {
            background-image:none !important
        }

        .st-wrapper-table {
            width: 100% !important;
            max-width: 480px !important;
            margin:0 auto
        }
    }

    #MessageViewBody .st-module-wrapper-table {
        margin-top:-1px
    }

    @media (max-width: 649px) and(min-width: 481px) {
        .st-module-wrapper-table {
            margin-top:-1px !important
        }
    }

    div > u + .body .st-module-wrapper-table {
        margin-top: 0 !important
    }
    </style>
    <!--[if mso]><style>table{border-collapse:collapse}span.MsoHyperlink{mso-style-priority:99;color:inherit}span.MsoHyperlinkFollowed{mso-style-priority:99;color:inherit}ul,ol{margin:0!important}ol li,ul li{margin-top:0!important;margin-bottom:0!important;margin-left:40px!important}</style><![endif]-->
    <!--[if gte mso 9]><style>.st-mso-full-width{width:100%}</style><![endif]-->
    <!--[if IEMobile]><style type="text/css">.st-mso-full-width{width:100%}</style><![endif]-->
    <!--[if mso]><style>.monofont h1,h2,h3,h4,h5,h6,p,a,span,td,strong{font-family:IBM Plex Mono,monospace,Arial,sans-serif!important}</style><![endif]-->
    <!--[if mso]><style>h1,h2,h3,h4,h5,h6,p,a,span,td,strong{font-family:Helvetica,Arial,sans-serif!important}</style><![endif]-->
    <style>
    .minw-203 a {
        min-width:167px !important
    }

    .minw-228 a {
        min-width:192px !important
    }

    .minw-180 a {
        min-width:144px !important
    }

    .minw-60 {
        min-width:60px !important
    }

    .minw-33 {
        min-width:33px !important
    }

    .border-2px-right > table {
        border-right:solid 2px #10162f !important
    }

    .border-2px-top > table {
        border-top:2px solid #10162f !important
    }

    .border-12px-bottom > table {
        border-bottom:12px solid #10162f !important
    }

    .border-2px-bottom > table {
        border-bottom:2px solid #10162f !important
    }

    .border-2px-left > table {
        border-left:2px solid #10162f !important
    }

    .border-15px-left > table {
        border-left:14px solid #10162f !important
    }

    .lh-36 p {
        line-height:36px !important
    }

    .lh-36 span {
        line-height:36px !important
    }

    .text-align-left span {
        text-align:left !important
    }

    .dark-image {
        text-align:left !important
    }

    ul {
        padding-left:15px !important
    }

    ul li {
        list-style-position:outside !important
    }

    #MessageViewBody a {
        color: inherit;
        text-decoration: none;
        font-size: inherit;
        font-family: inherit;
        font-weight: inherit;
        line-height:inherit
    }

    @media (max-width: 480px) {
        .padding-top-12 {
            padding-top:12px !important
        }

        .vertical-padding-24 {
            padding-top: 24px !important;
            padding-bottom:24px !important
        }

        .padding-sides-22 {
            padding-left: 22px !important;
            padding-right:22px !important
        }

        .padding-bottom-56 {
            padding-bottom:56px !important
        }

        .padding-bottom-15 {
            padding-bottom:15px !important
        }

        .padding-bottom-50 {
            padding-bottom:50px !important
        }

        .padding-bottom-24 {
            padding-bottom:24px !important
        }

        .padding-top-25 {
            padding-top:25px !important
        }

        .padding-top-30 {
            padding-top:30px !important
        }

        .padding-top-20 {
            padding-top:20px !important
        }

        .padding-bottom-32 {
            padding-bottom:32px !important
        }

        .padding-sides-32 {
            padding-left: 32px !important;
            padding-right:32px !important
        }

        .padding-right-32 {
            padding-right:32px !important
        }

        .padding-left-34 {
            padding-left:34px !important
        }

        .padding-sides-bgimage .bgi-padding-left {
            width:22px !important
        }

        .padding-sides-bgimage .bgi-padding-right {
            width:22px !important
        }

        .reset-padding-sides {
            padding-left: 0 !important;
            padding-right:0 !important
        }

        .reset-padding-top {
            padding-top:0 !important
        }

        .padding-right-44 {
            padding-right:44px !important
        }

        .padding-left-42 {
            padding-left:42px !important
        }

        .padding-right-30 {
            padding-right:30px !important
        }

        .padding-left-22 {
            padding-left:22px !important
        }

        .padding-left-18 {
            padding-left:18px !important
        }

        .padding-right-22 {
            padding-right:22px !important
        }

        .center-element td {
            margin: 0 auto !important;
            text-align:center !important
        }

        .center-element {
            text-align:center !important
        }

        .center-element table {
            margin:0 auto !important
        }

        .center-element p {
            text-align:center !important
        }

        .center-element span {
            text-align:center !important
        }

        .center-image img {
            margin:0 auto !important
        }

        .left-align p {
            text-align:left !important
        }

        .left-align span {
            text-align:left !important
        }

        .small-font-mobile p {
            font-size: calc(100% - 10px) !important;
            line-height:1.2 !important
        }

        .small-font-mobile p span {
            font-size: calc(100% - 10px) !important;
            line-height:1.2 !important
        }

        .minw-98 {
            width: 98px !important;
            min-width: 98px !important;
            height: 21px !important;
            max-width:98px !important
        }

        .minw-98 img {
            width: 98px !important;
            min-width: 98px !important;
            height: 21px !important;
            max-width: 98px !important
        }
    }
    </style>
    <style>
    @media (prefers-color-scheme: dark) {
        .light-image {
            display:none !important
        }

        .dark-image {
            display:block !important
        }

        .dark-yellow-bttn {
            color: #10162f !important;
            background-color:#ffd300 !important
        }
    }

    @media (prefers-color-scheme: light) {
        .light-image {
            display:block !important
        }

        .dark-image {
            display:none !important
        }
    }

    [data-ogsc] .dark-image {
        display:block !important
    }

    [data-ogsb] .dark-image {
        display:block !important
    }

    [data-ogsc] .light-image {
        display:none !important
    }

    [data-ogsb] .light-image {
        display:none !important
    }

    [data-ogsc] .dark-yellow-bttn {
        color: #10162f !important;
        background-color:#ffd300 !important
    }

    [data-ogsb] .dark-yellow-bttn {
        color: #10162f !important;
        background-color: #ffd300 !important
    }
    </style>
</head>
"""

    html_body = f"""
    <body class="st-email-body st-center-gmail">
    <span style="color:transparent;visibility:hidden;display:none;opacity:0;height:0;width:0;font-size:0;">S: E-PAY ENTERSOFT ESRETAIL ERROR</span>
    <div style="font-size:0px; display:none; visibility:hidden; opacity:0; color:transparent; max-height:0px; height:0; width:0; mso-hide:all;"> &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; &zwnj; </div>
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FFFFFF" class="st-wrapper-table" style="width: 100%;">
        <tr>
            <td width="100%" valign="top" align="center" class="st-dynamic-981-5">
                <table role="presentation" border="0" cellpadding="0" cellspacing="0" align="center" width="650" class="st-wrapper st-wrapper-background st-module-wrapper-table" style="width: 650px;">
                    <tr>
                        <td width="100%" bgcolor="#FFF0E5" valign="top" class="padding-sides-22 vertical-padding-24" style="width: 100%; padding: 56px 60px 32px;">
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="530" class="st-mso-full-width st-mobile-full-width" style="width: 530px;">
                                <tr>
                                    <td width="100%" align="center" valign="top" style="width: 100%;">
                                        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                                            <tr>
                                                <td width="100%" valign="top" align="left" style="width: 100%; padding-bottom: 20px;">
                                                    <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/FT.png?raw=true" alt="FT Logo" style="width: 150px; height: 44px;">
                                                </td>
                                            </tr>
                                            <tr>
                                                <td width="100%" valign="top" align="center" class="st-dynamic-999-2" style="width: 100%;">
                                                    <span style="font-size: 44px; line-height: 53px; color: red;">E-PAY ERROR</span>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td width="100%" valign="top" align="center" class="st-dynamic-981-5">
                <table role="presentation" border="0" cellpadding="0" cellspacing="0" align="center" width="650" class="st-wrapper st-wrapper-background st-module-wrapper-table" style="width: 650px;">
                    <tr>
                        <td width="100%" bgcolor="#FFF0E5" valign="top" class="padding-sides-22" style="width: 100%; padding-right: 60px; padding-left: 60px;">
                            <table role="presentation" border="0" cellpadding="0" cellspacing="0" align="center" width="100%" style="width: 100%;">
                                <tr>
                                    <td width="100%" valign="top" align="left">
                                        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="530" class="st-mso-full-width st-mobile-full-width" style="width: 530px;">
                                            <tr>
                                                <td width="100%" align="center" valign="top" style="width: 100%;">
                                                    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                                                        <tr>
                                                            <td width="100%" valign="top" align="left" class="monofont" style="text-align: left; font-family: 'Suisse Intl Mono', 'IBM Plex Mono', 'Courier New', 'Lucida Grande'; color: #1557ff; font-size: 20px; font-weight: bold; letter-spacing: normal; line-height: 24px; padding-bottom: 8px; width: 100%;">
                                                                <p style="margin: 0px;">
                                                                    <span style="font-size: 20px; line-height: 24px; background-color: red; color: #fff0e5;">ALERT</span>
                                                                </p>
                                                            </td>
                                                        </tr>
<!--                                                        -->
                                                        <tr>
                                                            <td width="100%" valign="top" align="left" style="text-align: left; font-family: 'Apercu Pro', 'Work Sans', Helvetica, Arial, sans-serif; color: #000000; font-size: 16px; font-weight: normal; letter-spacing: normal; line-height: 24px; padding-bottom: 24px; width: 100%;">
                                                                <p style="margin: 0px;">
                                                                     <span style="font-size: 16px; line-height: 24px;">Αγαπητή ομάδα, εντοπίστηκε εγγραφή πληρωμής που περιέχει <b>σφάλματα</b>, τα οποία ενδέχεται να εμποδίσουν την ολοκλήρωση της διαδικασίας <b>κλεισίματος (Ζ)</b> από τον φορολογικό μηχανισμό το βράδυ. </span>
                                                                <br>
                                                                <br>
                                                                <table role="presentation" style="width: 100%; border-collapse: collapse;">
                                                                            <tr>
                                                                                <td style="border-bottom: 1px solid #2cb543; width: 40%;"></td>
                                                                                <td style="width: 20%; text-align: center; font-weight: bold; color: #2cb543;">
                                                                                    Ενέργειες
                                                                                </td>
                                                                                <td style="border-bottom: 1px solid #2cb543; width: 40%;"></td>
                                                                            </tr>
                                                                    </table>
                                                                <br>
                                                                <br>
                                                                    <table role="presentation" style="width: 100%; margin-bottom: 15px; border-collapse: collapse;">
                                                                        <tr>
                                                                            <td style="vertical-align: middle; width: 20px;">
                                                                                <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/diamond.png?raw=true" alt="Diamond" style="margin-right: 8px; width: 16px; height: 16px;">
                                                                            </td>
                                                                            <td style="vertical-align: middle; font-size: 14px; line-height: 20px; color: #000;">
                                                                                Διορθώστε την εγγραφή πληρωμής, ώστε να μην εμποδίζεται το κλείσιμο (Ζ).
                                                                            </td>
                                                                        </tr>
                                                                         <tr>
                                                                            <td style="vertical-align: middle; width: 20px;">
                                                                                <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/diamond.png?raw=true" alt="Diamond" style="margin-right: 8px; width: 16px; height: 16px;">
                                                                            </td>
                                                                            <td style="vertical-align: middle; font-size: 14px; line-height: 20px; color: #000;">
                                                                                Ενημερώστε για τις ενέργειες που πραγματοποιήσατε.
                                                                            </td>
                                                                        </tr>
                                                                        <tr>
                                                                            <td style="vertical-align: middle; width: 20px;">
                                                                                <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/diamond.png?raw=true" alt="Diamond" style="margin-right: 8px; width: 16px; height: 16px;">
                                                                            </td>
                                                                            <td style="vertical-align: middle; font-size: 14px; line-height: 20px; color: #000;">
                                                                                Επικοινωνήστε το πρόβλημα που προέκυψε και προτείνετε λύσεις για την αποφυγή παρόμοιων προβλημάτων στο μέλλον.
                                                                            </td>
                                                                        </tr>

                                                                    </table>

                                                                </p>
                                                                <p style="margin: 0px;">
                                                                    &zwnj;
                                                                    <br/>
                                                                </p>
                                                                <p style="margin: 0px;">
                                                                    <span style="font-size: 16px; line-height: 24px;">
                                                                        <table role="presentation" style="width: 100%; border-collapse: collapse;">
                                                                            <tr>
                                                                                <td style="border-bottom: 1px solid #2cb543; width: 30%;"></td>
                                                                                <td style="width: 40%; text-align: center; font-weight: bold; color: #2cb543;">
                                                                                    Στοιχεία για το ζήτημα
                                                                                </td>
                                                                                <td style="border-bottom: 1px solid #2cb543; width: 30%;"></td>
                                                                            </tr>
                                                                        </table>

                                                                        <br>
                                                                        <br>

                                                                        <!-- Πρώτο Πλαίσιο: DATE και TIME -->
                                                                        <table role="presentation" style="border: 1px solid #2cb543; border-radius: 12px; width: 100%; border-collapse: collapse; text-align: center; padding: 0;">
                                                                            <tr>
                                                                                <td style="width: 50%; font-weight: bold; color: #333; padding: 10px;">
                                                                                    <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/calendar.png?raw=true" alt="Calendar Icon" style="width: 20px; height: 20px;"><br>
                                                                                    DATE: {date}
                                                                                </td>
                                                                                <td style="width: 50%; font-weight: bold; color: #333; padding: 10px; border-left: 1px solid #2cb543;">
                                                                                    <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/wallclock.png?raw=true" alt="Clock Icon" style="width: 20px; height: 20px;"><br>
                                                                                    TIME: {time}
                                                                                </td>
                                                                            </tr>
                                                                        </table>
                                                                        <br>
                                                                        <br>
                                                                        <!-- Δεύτερο Πλαίσιο: Κατάστημα και ΦΗΜΑΣ -->
                                                                        <table role="presentation" style="border: 1px solid #2cb543; border-radius: 12px; width: 100%; border-collapse: collapse; text-align: center; padding: 0;">
                                                                            <tr>
                                                                                <td style="width: 50%; font-weight: bold; color: #333; padding: 10px;">
                                                                                    <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/store.png?raw=true" alt="Store Image" style="width: 100px; height: 100px;"><br>
                                                                                    Κατάστημα:<br>
                                                                                    {store_name}
                                                                                </td>
                                                                                <td style="width: 50%; font-weight: bold; color: #333; padding: 10px; border-left: 1px solid #2cb543;">
                                                                                    <img src="https://github.com/johnkommas/Wallpaper/blob/master/images/epay.png?raw=true" alt="Tax Machine Image" style="width: 100px; height: 86px;"><br>
                                                                                    ΦΗΜΑΣ:<br>
                                                                                    {retail_point}
                                                                                </td>
                                                                            </tr>
                                                                        </table>

                                                                        <br>
                                                                        <br>
                                                                        
                                                             Παρακαλώ για τις ενέργειές σας.
                                                                    </span>
                                                                </p>
                                                                <p style="margin: 0px;">
                                                                    &zwnj;
                                                                    <br/>
                                                                </p>
                                                                <p style="margin: 0px;">
                                                                    <span style="font-size: 16px; line-height: 24px;">Με εκτίμηση, </span>
                                                                </p>
                                                                <p style="margin: 0px;">
                                                                    <span style="font-size: 16px; line-height: 24px;">Τμήμα Μηχανογράφησης</span>
                                                                </p>
                                                                
                                                            </td>
                                                        </tr>

                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td width="100%" valign="top" align="center" class="st-dynamic-981-5">
                <table role="presentation" border="0" cellpadding="0" cellspacing="0" align="center" width="650" class="st-wrapper st-wrapper-background st-module-wrapper-table" style="width: 650px;">
                    <tr>
                        <td width="100%" bgcolor="#FFF0E5" valign="top" style="width: 100%;">
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="650" class="st-mso-full-width st-mobile-full-width" style="width: 650px;">
                                <tr>
                                    <td width="100%" align="center" valign="top" style="width: 100%;">
                                        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                                            <tr>
                                                <td width="100%" valign="top" align="center" style="padding: 0px; width: 100%;">
                                                    <p height="48" width="100%" style="mso-line-height-rule:exactly; mso-table-lspace:0pt; mso-table-rspace:0pt; text-size-adjust:100%; width: 100%; height: 48px; max-height: 48px; margin: 0px; font-size: 48px; line-height: 48px"> &nbsp; </p>
                                                    <img alt="" height="120"
                                                        src="https://raw.githubusercontent.com/johnkommas/CodeCademy_Projects/master/img/mail/order/emb24.png"
                                                        style="border: 0;">
                                                    <p height="48" width="100%" style="mso-line-height-rule:exactly; mso-table-lspace:0pt; mso-table-rspace:0pt; text-size-adjust:100%; width: 100%; height: 48px; max-height: 48px; margin: 0px; font-size: 48px; line-height: 48px"> &nbsp; </p>
                                                    
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td width="100%" valign="top" align="center" class="st-dynamic-981-5">
                <table role="presentation" border="0" cellpadding="0" cellspacing="0" align="center" width="650" class="st-wrapper st-wrapper-background st-module-wrapper-table" style="width: 650px;">
                    <tr>
                        <td width="100%" bgcolor="#FFFFFF" valign="top" class="padding-sides-22" style="width: 100%; padding: 72px 90px;">
                            <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="470" class="st-mso-full-width st-mobile-full-width" style="width: 470px;">
                                <tr>
                                    <td width="100%" align="center" valign="top" style="width: 100%;">
                                        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                                            <tr>
                                                <td width="100%" valign="top" align="left" style="text-align: left; font-family: 'Apercu Pro', 'Work Sans', Helvetica, Arial, sans-serif; color: #000000; font-size: 14px; font-weight: normal; letter-spacing: normal; line-height: 24px; width: 100%;">
                                                
                                                    <p style="margin: 0; text-align: center;">
                                                        <span style="font-size: 14px; line-height: 24px;">Copyright© Ioannis E. Kommas. All rights reserved.</span>
                                                    </p>
                                                
                                                </td>

                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <!--[if (!lte mso 19)|(!IE)]><!-->
        <tr>
            <td class="st-gmail-fix" style="background-color: #FFFFFF; line-height: 1px; height: 1px; min-width: 650px;">
                <img src="https://www.cdn1ve3zg.com/nk4vlec16o/en_us/images/spacer.gif" alt="" height="1" width="650" style="max-height: 1px; display: block; width: 650px; min-width: 650px; border: 0;">
            </td>
        </tr>
        <!--<![endif]-->
    </table>

</body>
"""

    html_end = "</html>"

    html = html_start + html_head + html_body + html_end
    return html

# test
# https://github.com/johnkommas/Wallpaper/blob/master/images/FT.jpeg?raw=true
# with open("test.html", "w") as f:
#     f.write(main_body('Elounda Market', 'ΤΑΜΕΙΟ Α',"19.04.2025 13:41:12" ))