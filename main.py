from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QPushButton,QLineEdit


def build_sentence():
    input_text=text.text()
    output_label.setText(input_text.capitalize()+".")


app=QApplication([])
window=QWidget()
window.setWindowTitle("Sentence Builder")

layout=QVBoxLayout()

text=QLineEdit()
layout.addWidget(text)

btn=QPushButton("Build")
layout.addWidget(btn)

btn.clicked.connect(build_sentence)

output_label=QLabel("")
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()
