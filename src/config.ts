import { info, profile } from './lib/data';
export const SITE_TITLE = info.name;
export const SITE_DESCRIPTION = profile.introduction.replace(/<[^>]*>/g, '');
