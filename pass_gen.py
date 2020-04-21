def pass_generate(pass_ori):
    """入力パスワードを同じ長さの文字列に変換する関数

    Parameters
    ----------
    pass_ori: list(int)
        変換対象のパスワード列を1文字ずつ10進数に変換したもの

    Returns
    -------
    string
        生成パスワード
    """
    pass_gen = []
    for i, dec_num in enumerate(pass_ori):
        """ アルゴリズム解説
        * パスワードに利用可能な文字列は主に半角英数字で以下にその10進数表記を示す
            - 0~9 = 48~57 : 10個
            - A~Z = 65~90 : 26個
            - a~z = 97~122 : 26個
        * 上記のように連番が３箇所あるので元パスワード配列の配列番号を3で割った余りにより処理を分ける
        """
        if (i % 3) == 0:
            pass_gen.append(chr(48 + (dec_num % 10)))
        elif (i % 3) == 1:
            pass_gen.append(chr(65 + (dec_num % 26)))
        else:
            pass_gen.append(chr(97 + (dec_num % 26)))
    return ''.join(pass_gen)

if __name__ == '__main__':
    pass_ori = [ord(i) for i in list(input())]
    print(pass_generate(pass_ori))
