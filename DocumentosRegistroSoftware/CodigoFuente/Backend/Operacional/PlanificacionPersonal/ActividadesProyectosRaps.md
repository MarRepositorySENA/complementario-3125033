```

//ENTITY ACTIVIDADESPROYECTOSRAPS
package com.persona.Backend.Entity.Operational.PlanificacionFormativa;

import com.persona.Backend.Entity.BaseEntity;
import com.persona.Backend.Entity.Operational.GestionFormativa.Rap;

import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "actividades_proyectos_raps")
public class ActividadesProyectosRaps extends BaseEntity {

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "actividad_proyecto_id", nullable = false, unique = false)
	private ActividadProyecto actividadProyectoId;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "rap_id", nullable = false, unique = false)
	private Rap rapId;

	public ActividadProyecto getActividadProyectoId() {
		return actividadProyectoId;
	}

	public void setActividadProyectoId(ActividadProyecto actividadProyectoId) {
		this.actividadProyectoId = actividadProyectoId;
	}

	public Rap getRapId() {
		return rapId;
	}

	public void setRapId(Rap rapId) {
		this.rapId = rapId;
	}

}
//IREPOSITORY ACTIVIDADESPROYECTOSRAPS
package com.persona.Backend.IRepository.Operational.PlanificacionFormativa;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.PlanificacionFormativa.ActividadesProyectosRaps;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IActividadesProyectosRapsRepository extends IBaseRepository<ActividadesProyectosRaps, Long>{

}


//ISERVICE ACTIVIDADESPROYECTOSRAPS
package com.persona.Backend.IService.Operational.PlanificacionFormativa;

import com.persona.Backend.Entity.Operational.PlanificacionFormativa.ActividadesProyectosRaps;
import com.persona.Backend.IService.IBaseService;

public interface IActividadesProyectosRapsService extends IBaseService<ActividadesProyectosRaps> {

}

//SERVICE ACTIVIDADESPROYECTOSRAPS
package com.persona.Backend.Service.Operational.PlanificacionFormativa;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.PlanificacionFormativa.ActividadesProyectosRaps;
import com.persona.Backend.IService.Operational.PlanificacionFormativa.IActividadesProyectosRapsService;
import com.persona.Backend.Service.BaseService;

@Service
public class ActividadesProyectosRapsService extends BaseService<ActividadesProyectosRaps> implements IActividadesProyectosRapsService{

}

//CONTROLLER ACTIVIDADESPROYECTOSRAPS
package com.persona.Backend.Controller.Operational.PlanificacionFormativa;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.PlanificacionFormativa.ActividadesProyectosRaps;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/planificacion_formativa/actividades_proyectos_raps")
public class ActividadesProyectosRapsController extends BaseController<ActividadesProyectosRaps>{

}


```