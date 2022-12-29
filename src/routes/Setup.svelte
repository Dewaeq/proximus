<script lang="ts">
    import Api from "../services/api";
    import StatusWidget from "../components/StatusWidget.svelte";
    import Warning from "../components/Warning.svelte";
    import type Status from "../models/status.js";

    const api = new Api();
    let isConnecting = false;

    let ssid: string;
    let pass: string;

    const connect = async () => {
        isConnecting = true;
        await api.connect(ssid, pass);
    };

    export let status: Status;
</script>

<div id="content">
    <h1>AP Setup</h1>

    <p>
        Use the form below to connect to your router. The station will restart
        while it's establishing a connection to your network and you can follow
        along on the integrated display.
    </p>

    <StatusWidget {status} />

    <div class="inputs">
        <div class="input-box">
            <label for="ssid">Network: </label>
            <input bind:value={ssid} name="ssid" type="text" />
        </div>
        <div class="input-box">
            <label for="pass">Password: </label>
            <input bind:value={pass} name="pass" type="password" />
        </div>
    </div>

    <button class="btn" on:click={connect}>Connect</button>
    {#if isConnecting}
        <Warning
            text="Station will now restart and try to establish a connection. See the
    integrated display for details and results."
        />
    {/if}
</div>

<style>
    #content {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .input-box {
        display: flex;
        justify-content: space-between;
        width: 100%;
        padding: 7px 0;
    }

    .input-box > label {
        padding-right: 12px;
    }

    .btn {
        background-color: rgb(15, 211, 31);
        color: white;
        border: 3px solid transparent;
        border-radius: 7px;
        margin-top: 20px;
        padding: 7px 5px;
        width: 8rem;
        cursor: pointer;
        font-weight: bold;
        transition: all 200ms ease;
    }
    .btn:hover {
        background-color: white;
        color: rgb(15, 211, 31);
        border: 3px solid rgb(15, 211, 31);
    }
</style>
