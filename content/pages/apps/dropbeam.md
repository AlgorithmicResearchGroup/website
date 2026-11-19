Title: Dropbeam
Slug: dropbeam
Url: work/dropbeam.html
Save_as: work/dropbeam.html
Template: app-detail
Work_kind: apps
App_key: dropbeam
Card_title: Dropbeam
Summary: Private, account-free file transfer for desktop. A short one-time code connects two people, and the files travel over an authenticated encrypted connection instead of sitting in a cloud drive.
Platform: macOS · Windows · Linux
Discipline: File transfer / Private by design
Practice: Design & development
Availability: Coming soon
Icon: images/apps/dropbeam/dropbeam-icon.svg
App_question: Why should sending someone a file require an account, a device directory, or a permanent copy on a platform?
App_approach: Pair two computers with a short one-time code, encrypt the transfer, and let the file move directly when the network allows it.
Cta_label: Coming soon
Cta_title: Send the file, not your identity.
Cta_note: Dropbeam is being prepared for the ARG Store. No account, subscription, or device list required.
App_order: 04

## File sharing without joining anything.

Most file-sharing tools begin by turning both people into users of the same service. Upload the file. Create an account. Invite someone into a folder. Leave a durable copy behind on infrastructure neither person controls.

Dropbeam begins with the two people instead. The sender chooses one or more files and receives a short, human-readable code. The recipient opens Dropbeam, enters that code, and the transfer begins. There is no account to create, contact list to maintain, or cloud folder to clean up later.

The code is single-use. It exists to introduce one sender to one recipient for one transfer—not to become another permanent identity.

## A connection, not a storage product.

Dropbeam uses the Magic Wormhole protocol to create an authenticated encrypted connection between the two computers. It attempts a direct route first. When firewalls or network conditions make that impossible, an encrypted stream can pass through a transit relay instead.

A hosted rendezvous service is still involved in pairing the two sessions, and a relay may carry encrypted bytes when a direct connection cannot be made. Dropbeam does not pretend the internet disappears. The privacy boundary is more useful and more specific: the service helps make the connection, but it is not a cloud drive holding the finished files.

<div class="app-feature-grid">
    <section class="app-feature"><span class="mono">01 / One-time code</span><h3>No account handshake.</h3><p>Share a short code by text, email, or voice. The recipient enters it once to join that transfer.</p></section>
    <section class="app-feature"><span class="mono">02 / Encrypted transit</span><h3>The relay cannot read the file.</h3><p>File bytes travel through an authenticated encrypted connection, whether the route is direct or relayed.</p></section>
    <section class="app-feature"><span class="mono">03 / Streamed from disk</span><h3>No browser upload layer.</h3><p>The desktop backend streams selected files from disk. Their contents are never loaded into the app’s webview.</p></section>
    <section class="app-feature"><span class="mono">04 / Recovery</span><h3>Continue a large file.</h3><p>An interrupted single-file transfer can resume from locally saved partial progress with a new recovery code.</p></section>
</div>

## Local traces, made explicit.

Received files go to a folder the recipient chooses. Incomplete resumable files remain in Dropbeam’s local application data until the transfer finishes or the user discards them. The selected download location is also saved locally. Transfer history is limited to the current app session rather than becoming a hosted activity log.

Incoming filenames are sanitized, duplicate names are preserved with collision-safe filenames, and multiple files are unpacked into their own directory. If a multi-file transfer is interrupted, it restarts; resumable progress currently applies to single files.

Dropbeam is built as a desktop app for macOS, Windows, and Linux. The first public release is coming soon to the ARG Store.
