class mi:
    def camera(self):
        print("camera-8mp")
        return
    def display(self):
        print("full HD+")
        return
    def os(self):
        print("MIUI 10")
        return
class samsung(mi):
    def vediocall(self):
        print("can do vedio call")
        return
    def camera(self):
        print("camera 16MP")
        return
    def display1(self):
        print("AMO-LED")


mobile=samsung()
mobile.vediocall()
mobile.display()
mobile.camera()

        
        
