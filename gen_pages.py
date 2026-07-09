import os

base_template_top = """<!DOCTYPE html>
<html>

<head>
  <title>ASYNC Research Institute - Portal</title>
  <link rel="stylesheet" type="text/css" href="style.css">
  <script src="script.js"></script>
</head>

<body bgcolor="#cccccc" text="#000000" link="#0000ee" vlink="#551a8b" alink="#ff0000" onload="showDate()">
<div id="vga-screen">
  <center>
    <table width="620" border="0" cellpadding="0" cellspacing="0" bgcolor="#ffffff">
      <tr>
        <td bgcolor="#ffcc00" align="center" height="80">
          <img src="async_logo.png" alt="ASYNC Research Institute" width="540" height="200">
        </td>
      </tr>
      <tr>
        <td bgcolor="#000000" align="center" height="25">
          <font color="#ffff00" face="Arial" size="2"><b>WARNING: RESTRICTED ACCESS. UNAUTHORIZED PERSONNEL WILL BE
              PROSECUTED.</b></font>
        </td>
      </tr>
      <tr>
        <td padding="20">
          <table width="100%" border="0" cellpadding="15">
            <tr>
              <td valign="top" width="200" bgcolor="#e0e0e0">
                <center>
                  <font face="Arial"><b>Main Menu</b></font>
                </center>
                <hr width="80%">
                <ul>
                  <li><a href="index.html">Home Page</a></li>
                  <li><a href="about.html">About ASYNC</a></li>
                  <li><a href="kv31.html">Project KV31</a></li>
                  <li><a href="staff.html">Staff Directory</a></li>
                  <li><a href="safety.html">Safety Protocols</a></li>
                  <li><a href="contact.html">Contact Us</a></li>
                </ul>
                <br><br><br>
                <center>
                  <img src="globe.gif" alt="Spinning Globe" width="100"
                    height="100"><br>
                  <font size="1"><i>Best viewed in Netscape Navigator 3.0</i></font><br><br>
                  <table border="1" cellpadding="2" cellspacing="0" bgcolor="#000000">
                    <tr>
                      <td>
                        <font color="#00ff00" face="Courier" size="2">0024981</font>
                      </td>
                    </tr>
                  </table>
                  <font size="1">Visitors</font>
                </center>
              </td>
              <td valign="top">
"""

base_template_bottom = """              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td bgcolor="#333333" align="center" height="30">
          <font color="#ffffff" size="2" face="Courier" id="dateDisplay">Loading system date...</font>
        </td>
      </tr>
    </table>
  </center>
</div>
</body>

</html>
"""

pages = {
    "about.html": """                <center>
                  <h1>About ASYNC</h1>
                  <hr width="80%" align="center">
                </center>
                <p>
                  <font face="Times New Roman" size="3">
                    The <b>Async Research Institute</b> (often referred to as ASYNC) is a private research organization established in 1983. Initially focused on advanced MRI technology, our mandate rapidly expanded upon the discovery of anomalous spatial dynamics.
                  </font>
                </p>
                <p>
                  <font face="Times New Roman" size="3">
                    Our mission is to solve the most pressing anthropogenic issues of our time, including storage limits and residential space crises, by harnessing extradimensional space. 
                  </font>
                </p>
                <p>
                  <font face="Times New Roman" size="3">
                    Based in a classified facility in California, ASYNC stands at the forefront of human discovery, pushing the boundaries of physics beyond what was previously thought possible.
                  </font>
                </p>
                <br>
                <center><a href="index.html">[ Return to Main Menu ]</a></center>""",
    "kv31.html": """                <center>
                  <h1>Project KV31</h1>
                  <hr width="80%" align="center">
                </center>
                <p>
                  <font face="Times New Roman" size="3">
                    <b>Project KV31</b> is ASYNC's most ambitious undertaking: the development and operation of the Low-Proximity Magnetic Distortion System (LPMDS), commonly referred to as "The Machine" or "The Threshold".
                  </font>
                </p>
                <p>
                  <font face="Times New Roman" size="3">
                    Building upon prototypes from the early 1980s, the LPMDS utilizes concentrated magnetic waves to deform the fabric of reality, allowing stable access to an extradimensional space designated as "The Complex".
                  </font>
                </p>
                <p>
                  <font face="Times New Roman" size="3">
                    <b>Milestone:</b> The gateway to The Complex was successfully and formally opened on October 17, 1989.
                  </font>
                </p>
                <center>
                   <img src="portal.svg" alt="Gateway Simulation" width="200" height="150"><br>
                   <i><font size="2">LPMDS Distortion Simulation</font></i>
                </center>
                <br>
                <center><a href="index.html">[ Return to Main Menu ]</a></center>""",
    "staff.html": """                <center>
                  <h1>Staff Directory</h1>
                  <hr width="80%" align="center">
                </center>
                <p>
                  <font face="Times New Roman" size="3">
                    <b>Executive Leadership:</b><br>
                    - Ivan Beck, Director of Research<br>
                  </font>
                </p>
                <p>
                  <font face="Times New Roman" size="3">
                    <b>Project KV31 Key Personnel:</b><br>
                    - Marvin E. Leigh, Lead Researcher<br>
                    - Peter Tench, Field Researcher<br>
                    - Mark Blume, Technician<br>
                    - Clyde, Supervisor<br>
                  </font>
                </p>
                <p>
                  <font face="Times New Roman" size="3">
                    <i>Note: All other staff listings are classified and require Level 3 Clearance. Please see administration for inquiries regarding missing personnel.</i>
                  </font>
                </p>
                <br>
                <center><a href="index.html">[ Return to Main Menu ]</a></center>""",
    "safety.html": """                <center>
                  <h1>Safety Protocols</h1>
                  <hr width="80%" align="center">
                </center>
                <p>
                  <font face="Times New Roman" size="3">
                    <b>MANDATORY DIRECTIVES FOR THE COMPLEX:</b>
                  </font>
                </p>
                <ul>
                  <li><font face="Times New Roman" size="3"><b>Class A Hazmat Suits</b> are strictly required for all expeditions beyond the Threshold.</font></li>
                  <li><font face="Times New Roman" size="3">Expedition teams must consist of a minimum of <b>three (3) personnel</b> at all times.</font></li>
                  <li><font face="Times New Roman" size="3">Never approach the Threshold or operate the LPMDS without direct supervision from a Level 3 clearance officer.</font></li>
                  <li><font face="Times New Roman" size="3">Maintain visual contact with the tether line. Do not deviate from marked paths.</font></li>
                </ul>
                <p>
                  <font face="Times New Roman" size="3">
                    Failure to adhere to these protocols may result in permanent disorientation or disciplinary action.
                  </font>
                </p>
                <br>
                <center><a href="index.html">[ Return to Main Menu ]</a></center>""",
    "contact.html": """                <center>
                  <h1>Contact ASYNC</h1>
                  <hr width="80%" align="center">
                </center>
                <p>
                  <font face="Times New Roman" size="3">
                    Please fill out the form below to submit an inquiry to Administration.
                  </font>
                </p>
                <center>
                  <table border="1" cellpadding="5" bgcolor="#f0f0f0">
                    <tr>
                      <td><b>Name:</b></td>
                      <td><input type="text" size="25"></td>
                    </tr>
                    <tr>
                      <td><b>Department:</b></td>
                      <td><input type="text" size="25"></td>
                    </tr>
                    <tr>
                      <td><b>Message:</b></td>
                      <td><textarea rows="4" cols="30"></textarea></td>
                    </tr>
                    <tr>
                      <td colspan="2" align="center">
                        <input type="button" value="Send Message" onclick="alert('ERROR: Mail server unreachable. Connection to Sector 4 severed.')">
                      </td>
                    </tr>
                  </table>
                </center>
                <br>
                <center><a href="index.html">[ Return to Main Menu ]</a></center>"""
}

target_dir = "/Users/yoki/Downloads/Async-Web"

for filename, content in pages.items():
    filepath = os.path.join(target_dir, filename)
    with open(filepath, "w") as f:
        f.write(base_template_top + content + base_template_bottom)
    print(f"Created {filename}")
