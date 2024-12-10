from g4f.client import Client

def get_res_ai(content):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": content}],
    )

    res_id = []

    for i, j in enumerate(response.choices[0].message.content.replace("#", "").replace("*", "").replace("(", "").replace(")", "").split()):
        if j == "Id:":
            res_id.append(i+1)

    res_id_bim = []

    for i in res_id:
        res_id_bim.append(response.choices[0].message.content.replace("#", "").replace("*", "").replace("(", "").replace(")", "").split()[i])

    return res_id_bim