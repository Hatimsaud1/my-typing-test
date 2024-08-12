from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    test_text = "بسم الله الرحمن الرحيم لا اله الا الله حسبنا الله ونعم الوكيل ربي اجعلني مقيم الصلاة ومن ذريتي ربنا وتقبل دعاء ربنا اغفرلي ولوالدي وللمؤمنين وللمؤنين يوم يقوم الحساب"
    return render_template('index.html', test_text=test_text)

if __name__ == '__main__':
    app.run(debug=True)
