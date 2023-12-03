<script lang="ts">
    import { onMount } from "svelte";

    import Empty from "../../components/Empty.svelte";
    import Search from "../../components/Search.svelte";
    import Table from "../../components/Table.svelte";

    import { inventories, filteredInventories, searchKeyword } from "./store";

    // If there's `name` search param, set it to `searchKeyword` store.
    // This would allow user to filter the inventories directly if the user
    // typed in the full URL
    const searchParams = new URLSearchParams(window.location.search);
    searchKeyword.set(searchParams.get("name") || "");

    onMount(async () => {
        fetch("/api/inventory")
            .then((response) => response.json())
            .then((data) => inventories.set(data))
            .catch((error) => {
                console.log(error);
                return [];
            });
    });
</script>

<div class="row mt-3">
    <div class="col-12">
        <div class="card shadow">
            <div class="card-body">
                <Search {searchKeyword} />
                <br />
                {#if $filteredInventories.length}
                    <Table inventories={$filteredInventories} />
                {:else}
                    <Empty />
                {/if}
            </div>
        </div>
    </div>
</div>
