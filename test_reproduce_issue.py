#!/usr/bin/env python3
"""
Reproducer for pytest 6.0.0rc1 issue: capfd.readouterr() converts \r to \n
"""

def test_capfd_includes_carriage_return(capfd):
    print('Greetings from DOS', end='\r')
    out, err = capfd.readouterr()
    assert out.endswith('\r'), f"Expected output to end with \\r, but got {repr(out)}"

def test_capfd_preserves_carriage_return_mixed(capfd):
    print('Line 1\rLine 2\nLine 3\r\nLine 4', end='\r')
    out, err = capfd.readouterr()
    print(f"Captured output: {repr(out)}")
    assert '\r' in out, f"Expected \\r to be preserved in output, but got {repr(out)}"
    assert out.endswith('\r'), f"Expected output to end with \\r, but got {repr(out)}"

def test_capsys_includes_carriage_return(capsys):
    print('Greetings from DOS', end='\r')
    out, err = capsys.readouterr()
    assert out.endswith('\r'), f"Expected output to end with \\r, but got {repr(out)}"