from core.dir import manageDir
class start:
    fiels  = ['test grgeg (qefqefqef qgqrgr)','[fqefqef] test grgeg' , 'test grgeg', 'test grgeg (fwefwfwef)', 'fqefqeff' , '[fqefqe] feqfeqf (fewfwef wgwrgwrg)']

    def run(self):
        self.manageDirByLoop();

    def manageDirByLoop(self):
        for i in self.fiels:
            manageDir(i).set()
