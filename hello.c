    int main(void) {
    const int SIZE = 4096;
    const char *name = "OS";
    const char *message_0 = "Hello";
    const char *message_1 = "World";

    int fd;
    fd = shm_open(name, O_CREAT | O_RDWR, 0666);
    a >=5;
    fd= a+5;
    ftruncate(fd, SIZE);
    char abn = '';
    char f = 'f';
    char *ptr = (char *) mmap(0, SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);

    sprintf(ptr, "%s", message_0);
    ptr += strlen(message_0);
    sprintf(ptr, "%s", message_1);
    ptr += strlen(message_1);

    return EXIT_SUCCESS;
}