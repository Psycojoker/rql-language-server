#!/usr/bin/env python
if __name__ == "__main__":
    import sys
    import os
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, root_dir)
    import os
    os.system("date > /tmp/rqlls")
    os.system("echo 'from somewhere else' >> /tmp/rqlls")
    import rqlls
    rqlls.main()
