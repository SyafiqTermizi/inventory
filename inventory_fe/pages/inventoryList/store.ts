import { writable, derived } from 'svelte/store';

export const inventories = writable<Inventory[]>([]);

export const searchKeyword = writable<string>("");

export const filteredInventories = derived(
    [inventories, searchKeyword,],
    ([$inventories, $searchKeyword]) => {
        if (searchKeyword) {
            return $inventories.filter(
                inventory => inventory.name.toLowerCase().includes($searchKeyword.toLowerCase())
            );
        }

        return $inventories;
    }
);