def get_txt(user):
        with open("AI//data.txt", encoding="utf-8") as file:
                res = file.read()

        txt = f"""
        {user}
        {res}
        """

        return txt