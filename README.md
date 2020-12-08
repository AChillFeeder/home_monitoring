# Home monitoring app
### It's self-explanatory, an app that allows you to monitor your own house!

Using your computer and the online plateform at your disposition you could keep an eye on what happens around your device.
The program only supports a webcam but more devices will be supported, microphones, mouse motion when you're not using your computer...

You can take a read at the source code, it's on the simpler side. I'm using cv2 due to it being the most used (python doesn't have that many camera modules anyways) and the most flexible (so I'm not restricted by the libraries' limitations when I'm adding new features), and Flask for being suited for small (yet scalable) web apps, I really like Flask over Django since it allows me to be much more in control over my code and my files structures, Django feels very rigid and even though it's popular it wouldn't suit smaller apps like this one, maybe I need more learning on that side.

The code structure is pretty basic, a MODULES.PY file has the basic/low-level functions that MAIN.PY will use, making for a somewhat clear and concise code, there might be a Design Pattern that would've suited my program and made it much more manageable and scalable but I didn't find one yet, if I do I might be refactoring my code, or the necessary parts at the very least.

I don't know if there actually is a developper out there interested in this code, but if you want to use a part of the program (or all of it for that matter) then feel free to do so, I hope my code will make someone's work easier and I wonder what kind of projects they'd be working with!

### NEXT THINGS TO LEARN:
Django
Popular design patterns

