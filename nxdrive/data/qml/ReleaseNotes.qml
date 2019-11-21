import QtQuick 2.13

Rectangle {
    width: 600
    height: 400

    Text {
        text: manager.release_notes()
    }
}
