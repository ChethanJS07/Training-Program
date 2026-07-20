## Assignment 7 - ADB Troubleshooting

---

### Scenario

### You execute:

```bash
󰣇 ~ ❯ adb devices
List of devices attached

213375225E0307 device
222945225D0072 unauthorized
```

---

#### 1. Why is one device shown as unauthorized?

The device 222945225D0072 shows as unauthorized because the RSA fingerprint prompt on the device was not accepted when you first connected it to this computer.
When you connect an Android device to a new computer with USB Debugging enabled, Android displays a dialog asking you to allow USB debugging and trust the computer's RSA key fingerprint.

If you:

- Click "Cancel" or "Deny"

- Or don't respond to the prompt

- Or the prompt didn't appear due to a UI issue

Then the device remains in an unauthorized state. The computer has no permission to send ADB commands to that device.

---

#### 2. How would you resolve this issue?

- Step 1: Check the device screen
  Unlock the device and look for the USB Debugging authorization prompt.
  If it appears, check "Always allow from this computer" and click "OK".

- Step 2: If the prompt doesn't appear
  - Disconnect the USB cable and reconnect it.
    - Or restart ADB server:

  ```bash
  adb kill-server
  adb start-server
  Then run adb devices again to trigger the prompt.
  ```

  - Then run adb devices again to trigger the prompt.

---

#### 3. Can automation continue on the unauthorized device? Justify your answer.

No, automation cannot continue on the unauthorized device.

Justification:

- An unauthorized device does not permit ADB commands. This is a deliberate security feature.

---
