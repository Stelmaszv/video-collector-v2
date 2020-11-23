from core.dir import ManageDir
class start:
    fiels  = ['test grgeg (qefqefqef qgqrgr)','[fqefqef] test grgeg' , 'test grgeg', 'test grgeg (fwefwfwef and dqwdqf)', 'fqefqeff' , '[fqefqe] feqfeqf (fewfwef wgwrgwrg)']

    def run(self):
        self.manageDirByLoop();

    def manageDirByLoop(self):
        for i in self.fiels:
            ManageDir(i).set()
