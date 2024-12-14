from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render

from ..models import HOSTILITY, Location, Organization, Character, Event, Note
from .utils import *


RELATED_ORGANIZATIONS = "related_organizations"


# /campaigns/<int:campaign_id>/organizations/
@login_required
def organizations(req: HttpRequest, campaign_id: int) -> HttpResponse:
    campaign_opt = get_campaign_opt(campaign_id, req.user)
    if isinstance(campaign_opt, HttpResponse):
        return campaign_opt

    context = {
        ASSET: ASSET_URL,
        CSS: CSS_FILE,
        CURRENT_USER: req.user,
        CURRENT_CAMPAIGN: campaign_opt,
        ORGANIZATIONS: Organization.objects.filter(campaign=campaign_opt),
    }
    return render(req, "campaigns/organizations/index.html", context)


# /campaigns/<int:campaign_id>/organizations/new/
@login_required
def organizations_new(req: HttpRequest, campaign_id: int) -> HttpResponse:
    campaign_opt = get_campaign_opt(campaign_id, req.user)
    if isinstance(campaign_opt, HttpResponse):
        return campaign_opt

    if req.method == "GET":
        context = {
            ASSET: ASSET_URL,
            CSS: CSS_FILE,
            CURRENT_USER: req.user,
            CURRENT_CAMPAIGN: campaign_opt,
            LOCATIONS: Location.objects.filter(campaign=campaign_opt),
            ORGANIZATIONS: Organization.objects.filter(campaign=campaign_opt),
        }
        return render(req, "campaigns/organizations/new.html", context)
    # else it's POST, and it's a new organization request
    return organization_form(req, campaign_opt)


# /campaigns/<int:campaign_id>/organizations/<int:organization_id>/
@login_required
def organizations_id(req: HttpRequest, campaign_id: int, organization_id: int) -> HttpResponse:
    campaign_opt = get_campaign_opt(campaign_id, req.user)
    if isinstance(campaign_opt, HttpResponse):
        return campaign_opt
    organization_opt = get_campaign_field_opt(Organization, organization_id, campaign_opt)
    if isinstance(organization_opt, HttpResponse):
        return organization_opt

    context = {
        ASSET: ASSET_URL,
        CSS: CSS_FILE,
        CURRENT_USER: req.user,
        CURRENT_CAMPAIGN: campaign_opt,
        CURRENT_ORGANIZATION: organization_opt,
        RELATED_ORGANIZATIONS: organization_opt.related_organizations.all(),
        CHARACTERS: Character.objects.filter(organizations=organization_opt),
        EVENTS: Event.objects.filter(involved_organizations=organization_opt),
        NOTES: Note.objects.filter(organizations=organization_opt),
    }
    return render(req, "campaigns/organizations/organization.html", context)


# /campaigns/<int:campaign_id>/organizations/<int:organization_id>/edit/
@login_required
def organizations_edit(req: HttpRequest, campaign_id: int, organization_id: int) -> HttpResponse:
    campaign_opt = get_campaign_opt(campaign_id, req.user)
    if isinstance(campaign_opt, HttpResponse):
        return campaign_opt
    organization_opt = get_campaign_field_opt(Organization, organization_id, campaign_opt)
    if isinstance(organization_opt, HttpResponse):
        return organization_opt

    if req.method == "GET":
        context = {
            ASSET: ASSET_URL,
            CSS: CSS_FILE,
            CURRENT_USER: req.user,
            CURRENT_CAMPAIGN: campaign_opt,
            CURRENT_ORGANIZATION: organization_opt,
            RELATED_ORGANIZATIONS: organization_opt.related_organizations.all(),
            LOCATIONS: Location.objects.filter(campaign=campaign_opt),
            ORGANIZATIONS: Organization.objects.filter(campaign=campaign_opt)\
                                               .exclude(id=organization_opt.id),
        }
        return render(req, "campaigns/organizations/edit.html", context)
    # else it's POST, and it's an edit organization request
    return organization_form(req, campaign_opt, organization_opt)


# /campaigns/<int:campaign_id>/organizations/<int:organization_id>/delete/
@login_required
def organizations_delete(req: HttpRequest, campaign_id: int, organization_id: int) -> HttpResponse:
    campaign_opt = get_campaign_opt(campaign_id, req.user)
    if isinstance(campaign_opt, HttpResponse):
        return campaign_opt
    organization_opt = get_campaign_field_opt(Organization, organization_id, campaign_opt)
    if isinstance(organization_opt, HttpResponse):
        return organization_opt

    organization_opt.delete()
    return redirect(f"/campaigns/{campaign_id}/organizations/")
