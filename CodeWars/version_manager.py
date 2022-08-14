class VersionManager:
    def __init__(self, version: str | None = None):
        self.str_version = self.is_correct_version(version)
        self.MAJOR = int(self.mmp()[0][1])
        self.MINOR = int(self.mmp()[1][1]) if self.length() > 0 else 0
        self.PATCH = int(self.mmp()[2][1]) if self.length() > 1 else 0
        self.version = f"{self.MAJOR}.{self.MINOR}.{self.PATCH}"
        self.rollback_version = None

    @classmethod
    def is_correct_version(cls, version):
        if not version:
            version = "0.0.1"
        ver3 = version.split('.')
        version = '.'.join(ver3[:3])
        if not set(list(version)) <= {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}:
            raise ValueError("Error occured while parsing version!")
        return version

    def length(self):
        return self.str_version.count('.') if self.str_version.count('.') < 3 else 2

    def mmp(self):
        rel_types = ('MAJOR', 'MINOR', 'PATCH')
        tmp = list(zip(rel_types, self.str_version.split('.')))
        return tmp

    def major(self):
        self.rollback_version = self.version
        self.MAJOR = self.MAJOR + 1
        self.MINOR = 0
        self.PATCH = 0
        self.version = f"{self.MAJOR}.{self.MINOR}.{self.PATCH}"
        return self

    def minor(self):
        self.rollback_version = self.version
        self.MINOR = self.MINOR + 1
        self.PATCH = 0
        self.version = f"{self.MAJOR}.{self.MINOR}.{self.PATCH}"
        return self

    def patch(self):
        self.rollback_version = self.version
        self.PATCH = self.PATCH + 1
        self.version = f"{self.MAJOR}.{self.MINOR}.{self.PATCH}"
        return self

    def rollback(self):
        if self.rollback_version is None:
            raise ValueError("Cannot rollback!")
        else:
            self.version = self.rollback_version
            return self

    def release(self):
        return self.version


if __name__ == '__main__':
    v1 = VersionManager('0')
    print(v1.release())
    print(v1.major().rollback().release())