<script lang="ts">
    import { onMount } from "svelte";

    import Table from "../../components/Table.svelte";
    import Search from "../../components/Search.svelte";

    import { inventories, filteredInventories, searchKeyword } from "./store";

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
        <Search {searchKeyword} />
    </div>
</div>

<div class="row mt-3">
    <div class="col-12">
        <div class="card">
            <div class="card-body">
                <Table inventories={$filteredInventories} />
            </div>
        </div>
    </div>
</div>
