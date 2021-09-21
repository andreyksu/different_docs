screen = Screen(0)
file = screen.capture(<наименование региона>)
subprocess.Popen(['cp', file, '/home/user1'])    