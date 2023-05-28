# start only after metadata;
# concatenate wrapped msgstr to one line, so that opencc may convert by phrases accurately
BEGIN {
    start = 0
    remove = 0
}
/^msgstr "/ {
    if (start == 0) start = 1
}
{
    if (start == 0) next
}
/^msgstr ""$/ {
    printf("msgstr \"")
    remove = 1
    next
}
/^".+"$/ {
    if (remove == 1) {
        printf("%s", substr($0, 2, length($0) - 2))
        next
    }
}
/^(#.*|)$/ {
    if (remove == 1) {
        printf("\"\n")
        remove = 0
    }
}
{
    print $0
}
