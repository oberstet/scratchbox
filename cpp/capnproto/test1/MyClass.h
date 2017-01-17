class MyClass {
public:
    MyClass(int i = -99) : m_myint(i) {}

    int GetMyInt() { return m_myint; }
    void SetMyInt(int i) { m_myint = i; }

public:
    int m_myint;
};
