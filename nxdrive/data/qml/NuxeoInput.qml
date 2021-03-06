import QtQuick 2.13

TextInput {
    id: control
    property string placeholderText
    property string lineColor: nuxeoBlue

    font.pointSize: point_size
    wrapMode: TextInput.Wrap
    selectionColor: teal
    horizontalAlignment: TextInput.AlignLeft
    verticalAlignment: TextInput.AlignVCenter
    selectByMouse: true

    Rectangle {
        color: control.focus ? control.lineColor : lightGray
        width: control.width; height: 1
        anchors.bottom: parent.bottom
    }

    ScaledText {
        text: control.placeholderText
        color: lightGray
        visible: !control.text
        font: control.font

        anchors {
            bottom: parent.bottom
            bottomMargin: 3
        }
    }
}
