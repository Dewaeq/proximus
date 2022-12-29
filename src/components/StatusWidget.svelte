<script lang="ts">
    import type Status from "src/models/status.js";


    export let status: Status;
</script>

<div id="content">
    <p>Connected to wifi: {status.connected}</p>
    <p>Station id: {status.id}</p>
    <p>IP: {status.ip}</p>
    <p>SSID: {status.ssid}</p>
</div>