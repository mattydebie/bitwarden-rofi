from subprocess import Popen, PIPE


class Keyctl():

    def __init__(self):
        self._key = 'bw_session'

    def purge(self):
        Popen(['keyctl', 'purge', 'user', self._key], stdout=PIPE)

    def get(self):
        key_id = int(Popen(['keyctl', 'request', 'user', self._key], stdout=PIPE, stderr=PIPE).communicate()[0])
        session = Popen(['keyctl', 'pipe', "{}".format(key_id)], stdout=PIPE, stderr=PIPE).communicate()[0]
        return session.strip()

    def set(self, session):
        self.purge()
        ps = Popen(['keyctl', 'add', 'user',  self._key, session, '@u'], stdout=PIPE)
        return int(ps.communicate()[0])
