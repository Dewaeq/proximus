<script lang="ts">
    import type Status from "../models/status.js";
    import Header from "../components/Header.svelte";
    import StatusWidget from "../components/StatusWidget.svelte";
    import Warning from "../components/Warning.svelte";
    import Api from "../services/api.js";

    const api = new Api();
    let isDisconnecting = false;

    const disconnect = async () => {
        isDisconnecting = true;
        await api.disconnect();
    };

    export let status: Status;
</script>

<div>
    <Header />

    <div id="content">
        <StatusWidget {status} />

        <button class="danger" on:click={disconnect}>
            Disconnect from WiFi
        </button>
        {#if isDisconnecting}
            <Warning
                text="Disconnecting from wifi and restarting station... Please connect
        to the newly created acces point to configure the station."
            />
        {/if}
    </div>
</div>

<style>
    #content {
        margin: auto;
        display: flex;
        flex-direction: column;
        align-content: center;
        align-items: center;
    }

    .danger {
        background-color: rgb(209, 45, 16);
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

    .danger:hover {
        background-color: white;
        color: rgb(209, 45, 16);
        border: 3px solid rgb(209, 45, 16);
    }
</style>
