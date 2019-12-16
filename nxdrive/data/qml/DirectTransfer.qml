import QtQuick 2.13
import QtQuick.Controls 2.13
import QtQuick.Layouts 1.13
import QtQuick.Window 2.13
import QtQuick.Controls.Styles 1.4

Rectangle {
    id: directTransfer
    anchors.fill: parent
    color: lighterGray

    property string engineUid: ""

    signal setEngine(string uid)

    onSetEngine: engineUid = uid

    ColumnLayout {

        anchors {
            topMargin: 30
            bottomMargin: 30
            leftMargin: 30
            rightMargin: 30
            fill: parent
        }
        spacing: 10

        // Progression: percent
        ScaledText {
            Layout.alignment: Qt.AlignHCenter
            font.pointSize: 42
            text: "75%"
        }

        // Progression: transferred data and remote folder
        Text {
            text: qsTr("DIRECT_TRANSFER_DETAILS").arg() + tl.tr
        }

        // Progression: bar
        NuxeoProgressBar {
            id: progressBar
            Layout.fillWidth: true
            color: lightBlue
            height: 15
            value: 75  // progress || 0.0
        }
    }
}
