#!/usr/bin/python3

def parse_line(line: str):
    el = line.split("=")
    result = dict((value.strip().split(":") for value in el[1].split(", ")))
    result["name"] = el[0].strip()
    return result


def main():
    HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>periodic_table</title>
  <style>
    table{{
      border-collapse: collapse;
    }}
    h4 {{
      text-align: center;
    }}
    ul {{
      list-style:none;
      padding-left:0px;
    }}
  </style>
</head>
<body>
  <table>
    {body}
  </table>
</body>
</html>
"""

    TEMPLATE = """
      <td style="border: 1px solid black; padding:10px">
        <h4>{name}</h4>
        <ul>
          <li>No {number}</li>
          <li>{small}</li>
          <li>{molar}</li>
          <li>{electron} electron</li>
        </ul>
      </td>
"""

    body = "<tr>"
    f = open("periodic_table.txt", "r")
    periodic_table = [(parse_line(line)) for line in f.readlines()]
    f.close()
    position = 0
    for dic in periodic_table:
        if position > int(dic["position"]):
            body += "    </tr>\n    <tr>"
            position = 0
        for _ in range(position, int(dic["position"]) - 1):
            body += "      <td></td>"
        position = int(dic["position"])
        body += TEMPLATE.format(
            name=dic["name"],
            number=dic["number"],
            small=dic["small"],
            molar=dic["molar"],
            electron=dic["electron"],
        )
    body += "    </tr>\n"
    f = open("periodic_table.html", "w")
    f.write(HTML.format(body=body))
    f.close()


if __name__ == '__main__':
    main()
