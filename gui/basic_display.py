import sys
import glob
from collections import deque
import serial
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QLabel
from PyQt6.QtCore import QThread, pyqtSignal
import pyqtgraph as pg

MAX_POINTS = 200

def list_ports():
    if sys.platform.startswith("win"):
        return [f"COM{i}" for i in range(1, 21)]
    return sorted(glob.glob("/dev/ttyACM*") + glob.glob("/dev/ttyUSB*"))


class SerialThread(QThread):
    value = pyqtSignal(float)
    error = pyqtSignal(str)

    def __init__(self, port, baud):
        super().__init__()
        self.port = port
        self.baud = baud
        self._running = False

    def run(self):
        try:
            ser = serial.Serial(self.port, self.baud, timeout=1)
            self._running = True
            while self._running:
                line = ser.readline().decode("utf-8", errors="replace").strip()
                if line:
                    try:
                        self.value.emit(float(line))
                    except ValueError:
                        pass
            ser.close()
        except Exception as e:
            self.error.emit(str(e))

    def stop(self):
        self._running = False
        self.wait()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Graph")
        self.resize(800, 400)
        self.thread = None
        self.data = deque([0.0] * MAX_POINTS, maxlen=MAX_POINTS)

        w = QWidget()
        self.setCentralWidget(w)
        layout = QVBoxLayout(w)

        controls = QHBoxLayout()
        self.port_combo = QComboBox()
        self.port_combo.addItems(list_ports() or ["No ports found"])
        self.baud_combo = QComboBox()
        self.baud_combo.addItems(["9600", "19200", "57600", "115200"])
        self.btn = QPushButton("Connect")
        self.btn.clicked.connect(self.toggle)
        self.status = QLabel("Disconnected")

        controls.addWidget(QLabel("Port:"))
        controls.addWidget(self.port_combo)
        controls.addWidget(QLabel("Baud:"))
        controls.addWidget(self.baud_combo)
        controls.addWidget(self.btn)
        controls.addWidget(self.status)
        controls.addStretch()
        layout.addLayout(controls)

        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setYRange(0, 1023)
        self.plot_widget.setLabel("left", "Value")
        self.plot_widget.setLabel("bottom", "Samples")
        self.plot_widget.showGrid(x=True, y=True, alpha=0.3)
        self.curve = self.plot_widget.plot(list(self.data), pen=pg.mkPen("#00ff88", width=2))
        layout.addWidget(self.plot_widget)

    def toggle(self):
        if self.thread and self.thread.isRunning():
            self.thread.stop()
            self.thread = None
            self.btn.setText("Connect")
            self.status.setText("Disconnected")
        else:
            port = self.port_combo.currentText()
            baud = int(self.baud_combo.currentText())
            self.thread = SerialThread(port, baud)
            self.thread.value.connect(self.on_value)
            self.thread.error.connect(lambda e: self.status.setText(f"Error: {e}"))
            self.thread.start()
            self.btn.setText("Disconnect")
            self.status.setText(f"Connected — {port} @ {baud}")

    def on_value(self, v):
        self.data.append(v)
        self.curve.setData(list(self.data))

    def closeEvent(self, e):
        if self.thread:
            self.thread.stop()
        e.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())